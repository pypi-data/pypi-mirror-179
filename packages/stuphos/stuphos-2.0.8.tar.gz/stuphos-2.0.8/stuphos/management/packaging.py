# Extensions -- Executable.
from stuphos.etc.tools.strings import indent, nling

from base64 import b64encode


def b64_encode(s):
    # treat as bytes (for media content)
    # s = s.encode()

    return b64encode(s).decode()
# b64_encode = b64encode 

def quoteStringIf(s):
    return repr(s) if ':' in s else s

def renderPackageString(node):
    @nling
    def convert(node):
        type = node['type']

        if type == 'directory':
            i = node['children']

            if i:
                yield '%s:' % quoteStringIf(node['name'])

                s = [] # structures collection
                m = [] # media collection

                for c in i:
                    if c['type'] == 'structure':
                        s.append(c)
                        continue

                    elif c['type'] == 'media':
                        m.append(c)
                        continue

                    yield indent(convert(c))

                if s:
                    # yield indent('interfaces$:')
                    yield indent('interfaces:')

                    for c in s:
                        yield indent(convert(c), level = 2)

                if m:
                    # yield indent('media$:')
                    yield indent('media:')

                    for c in m:
                        yield indent(convert(c), level = 2)

            else:
                yield '%s: []' % quoteStringIf(node['name'])

        elif type == 'module':
            progr = node['programmer']
            if progr:
                yield '%s:' % quoteStringIf(node['name'])

                yield '    programmer: %s' % progr
                yield '    program::'

                yield indent(indent(node['program']))

            else:
                yield '%s::' % quoteStringIf(node['name'])
                yield indent(node['program'])

        elif type == 'structure':
            yield '%s::' % quoteStringIf(node['name'])
            yield indent(node['document'])

        elif type == 'media':
            content_type = node['content_type']
            if content_type:
                yield '%s:' % quoteStringIf(node['name'])

                yield '    content_type: %s' % content_type
                yield '    content::'

                content = node['content']
                if isinstance(content, str):
                    content = content.encode()

                yield indent(indent(b64_encode(content)))

            else:
                yield '%s::' % quoteStringIf(node['name'])
                yield indent(b64_encode(node['content']))

    def rewrite(node):
        # Transform tree root node name.
        if node['name'] is None:
            node['name'] = ''

        # debugOn()
        return node

    return convert(rewrite(node.exported))


class filesystem:
    # Represent a folder tree as structural input to the upload routine.

    def __init__(self, path, **kwd):
        self.path = path
        self.config = kwd

    def contents(self, path):
        value = path.open('r+b').read()
        try: return value.decode()
        except UnicodeDecodeError as e:
            print(f'[pkging$filesystem$items] {path}: {e}')
            return value

        return path.read() # .platformMapped

    def __len__(self):
        return len(self.path.listing)

    def __getitem__(self, name):
        if name in ['structures', 'interfaces']:
            try: return dict((p.basename, self.contents(p)) for p in
                             self.path(name).listing if not p.isdir)

            except FileNotFoundError:
                return dict()

        raise KeyError(name)

    def ignore(self, path):
        return path.basename in self.config.get('ignore', [])

    def iteritems(self):
        try: i = self.path.listing
        except FileNotFoundError: pass
        else:
            for p in i:
                if self.ignore(p):
                    continue

                if p.isdir:
                    yield (p.basename, self.__class__(p))
                else:
                    try: yield (p.basename, self.contents(p))
                    except UnicodeDecodeError as e:
                        print(f'[pkging$filesystem$items] {p}: {e}')

    def items(self):
        return list(self.iteritems())


def packageBuild(path, **config):
    @nling
    def w(o):
        if isinstance(o, (dict, filesystem)):
            for (name, value) in o.items():
                if isinstance(value, (list, tuple, dict, filesystem)):
                    yield f'{name}:'
                    yield indent(w(value))

                elif isinstance(value, bytes):
                    pass
                elif isinstance(value, str):
                    yield f'{name}::'
                    yield indent(value)

                else:
                    yield f'{name}: {repr(value)}'

        elif isinstance(o, (list, tuple)):
            if o:
                for value in o:
                    o = w(o)
                    o = o.split('\n')
                    if len(o) > 1:
                        yield '- ' + o[0]
                        yield indent('\n'.join[1:], tab = '  ')
                    else:
                        yield '- ' + o[0]
            else:
                yield '[]'

        else:
            yield repr(o)

    return w(filesystem(path, **config))


def setActivityProgrammer(core, path, name, progr):
    node = core.root.lookup(*(path + [name]))
    node.programmer = progr # XXX Todo: Programmer(progr)?

ALT_TYPES = ('structures', 'interfaces', 'media')

def uploadStructure(core, path, structure, set_programmers = False):
    structs = []
    media = []

    try: structs.extend(list(structure['structures'].items()))
    except KeyError: pass

    try: structs.extend(list(structure['interfaces'].items()))
    except KeyError: pass

    try: media.extend(list(structure['media'].items()))
    except KeyError: pass

    services = [(name, s) for (name, s) in structure.items()
                if name not in ALT_TYPES]

    def ensure(path):
        path = path.split('/')
        u = core.root.lookup

        for i in range(1, len(path)+1):
            folder = path[:i]

            try: u(*folder)
            except KeyError:
                core.addFolder('/'.join(folder[:i-1]), folder[-1])

    def install(path, struct, add, isMedia = False):
        # head = (path + '/') if path else ''

        if path:
            head = path + '/'
            ensure(path)
        else:
            head = ''

        for (name, s) in struct:
            name = str(name) # Because it gets __sqlrepr__ attr which might be complex.

            if isMedia:
                if isinstance(s, str):
                    s = b64_decode(s)
                    add(path, name, s)

                elif isinstance(s, (dict, filesystem)):
                    try: content = s['content']
                    except KeyError: pass
                    else:
                        try: content_type = s['type']
                        except KeyError: content_type = None

                        content = b64_decode(content)
                        add(path, name, content, content_type)

            else:
                if isinstance(s, str):

                    # print(f'{add.__name__}({path}/{name})')
                    add(path, name, s)

                elif isinstance(s, (dict, filesystem)):
                    try: content = s['program']
                    except KeyError: pass
                    else:
                        # If program is set, programmer must be set or it's added as a folder.
                        try: progr = s['programmer']
                        except KeyError: pass
                        else:
                            if len(s) == 2:
                                ensure(path)

                                # print(f'adding module: {path} {name} [{progr}]')

                                core.addModule(path, name, content)
                                if set_programmers:
                                    setActivityProgrammer(core, path, name, progr)

                                continue

                    # debugOn()

                    # print(f'adding folder: {path}/{name}')
                    # assert not '/' in name
                    if path:
                        ensure(path + '/' + name)
                    else:
                        ensure(name)

                    uploadStructure(core, head + name, s) # recurse


    # debugOn()
    install(path, structs, core.addStructure)
    install(path, services, core.addModule)
    install(path, media, core.addMedia, isMedia = True)


class fsPackageCore:
    # AgentSystem replacement for extracting packages to filesystem.
    class Node:
        pass

    class Folder(Node, dict):
        def lookup(self, path, *args):
            return self[path]

    def __init__(self, path):
        self.path = io.path(path)
        self.root = self.Folder()

    def addFolder(self, *args, **kwd):
        print('addfolder ' + str(args))
    def addModule(self, *args, **kwd):
        print('addmodule ' + str(args))
    def addStructure(self, *args, **kwd):
        print('addstructure ' + str(args))
    def addMedia(self, *args, **kwd):
        print('addmedia ' + str(args))


def packageUnpackTo(structure, dest_dir, mount_point = None):
    if isinstance(structure, str):
        from stuphos.language.document.interface import document
        structure = document(structure)

    core = fsPackageCore(dest_dir)
    uploadStructure(core, mount_point or '', structure)

def packageStreamUnpackTo(input, output, mount_point = None):
    '''
    --admin-script=ph.interpreter.mental.library.extensions.packageStreamUnpackTo \
    -x bin.package -x bin

    '''

    if input == '<stdin>':
        from sys import stdin as input
    else:
        input = open(input).read()

    return packageUnpackTo(input, output, mount_point = mount_point)


class normalContinue(Exception):
    def __init__(self, options, args):
        self.options = options
        self.args = args

        raise self


def unpackMain(options, args):
    if len(args) != 2:
        print('Usage: unpack <input package> <output path>')
        return

    (input, output) = args

    from stuphos.runtime.registry import getRegistry
    getRegistry(create = True) # stuphos.structure

    packageStreamUnpackTo(input, output, options.mount_point)


class project:
    def __init__(self, path, config, options):
        if config == '.':
            config = '.wmc'

        self.path = path = io.path(path)
        self.configpath = path(config)
        self.options = options

    @property
    def config(self):
        return self.configuration(self.path.config.cfgOf.value)

    class configuration(dict):
        def __init__(self, fileInputValue):
            pass

    def package(self, args):
        self.options.input_file = str(self.path)
        normalContinue(self.options, args)

    def upload(self, args):
        cfg = self.cfg


    @classmethod
    def Operate(self, options, args):
        assert args
        p = project(io.here, options.project, options)

        cmd = args[0]
        rest = args[1:]

        if cmd == 'upload':
            return p.upload(rest)
        elif cmd == 'package':
            return p.package(rest)


# @apply
# class defaultIgnore:
#     def __contains__(self, object):
#         return object in ['.git']

defaultIgnore = ['.git']


USAGE = \
'''
export PYTHONPATH=<path-to-common>:<path-to-stuphos>
python -m stuphos.management.packaging -o jhcore.package path/to/LambdaMOO/core.db

'''.rstrip()

def main(argv = None):
    # debugOn()
    from optparse import OptionParser
    parser = OptionParser(usage = USAGE)
    parser.add_option('-o', '--output-file', '--output')
    parser.add_option('-i', '--input-file', '--input')
    parser.add_option('-u', '--unpack', action = 'store_true')
    parser.add_option('--mount-point')
    parser.add_option('-p', '--project')
    parser.add_option('-v', '--verbose', action = 'store_true')
    (options, args) = parser.parse_args(argv)

    try: import op
    except Exception as e:
        print(f'{e.__class__.__name__}: {e}')

    try:
        if options.project:
            return project.Operate(options, args)

        if options.unpack:
            return unpackMain(options, args)

    except normalContinue as e:
        options = e.options
        args = e.args

    if options.input_file:
        assert not args
        input = options.input_file
    else:
        assert len(args) == 1
        input = args[0]

    if options.output_file:
        output = open(options.output_file, 'w')
    else:
        from sys import stdout as output

    import op

    output.write(str(packageBuild \
        (io.path(input),
         ignore = defaultIgnore)))

if __name__ == '__main__':
    main()
