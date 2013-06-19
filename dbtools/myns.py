import os.path
import ConfigParser
import sys

config_paths = ['~/.myns/databases']

def read_configs():
    parser = ConfigParser.RawConfigParser()
    parser.read(map(os.path.expanduser, config_paths))
    return parser

def mysql_cli_arguments(params):
    if 'host' in params:
        yield '-h'
        yield params['host']
    if 'user' in params:
        yield '-u'
        yield params['user']
    if 'password' in params:
        yield '-p'+params['password']
    if 'database' in params:
        yield params['database']

def main():
    if len(sys.argv) != 2:
        sys.stderr.write('\n'.join([
            'Usage:',
            '%(me)s DATABASE - print connection params for MySQL CLI tools',
            '%(me)s -l - list registered database names',
            '',
        ]) % {'me': sys.argv[0]})
        sys.exit(2)
    config = read_configs()
    if sys.argv[1] == '-l':
        for section in config.sections():
            print section
        sys.exit(0)

    name = sys.argv[1]
    if not config.has_section(name):
        sys.stderr.write('Database not found: %s\n' % name)
        sys.exit(1)
    
    arguments = mysql_cli_arguments(dict(config.items(name)))
    print ' '.join(arguments)
    sys.exit(0)

if __name__ == '__main__':
    main()
