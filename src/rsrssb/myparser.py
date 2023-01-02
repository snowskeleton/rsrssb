import sys
import configargparse


ARGUMENTS = [
    (
        ('--domain', '-d',),
        {
            "dest": 'domain',
            "type": str,
            "action": 'store',
            "help": 'Base URL (e.g., example.net)',
            "default": '',
        }
    ),
    (
        ('--root', '-r',),
        {
            "dest": 'root',
            "type": str,
            "action": 'store',
            "help": 'The directory structor of your website before the podcast (path/to/your/books): ',
            "default": '',
        }
    ),
    (
        ('--title', '-t',),
        {
            "dest": 'title',
            "type": str,
            "action": 'store',
            "help": 'The name of your feed',
            "default": '',
        }
    ),
    (
        ('--extension', '-e',),
        {
            "dest": 'extensions',
            "action": 'store',
            "nargs": '*',
            "type": str,
            "help": 'The format(s) of your audio files',
            "default": 'mp3',
        }
    ),
    (
        ('--output', '-o',),
        {
            "dest": 'outputFile',
            "action": 'store',
            "type": str,
            "help": 'Name of rss file to be created',
            "default": 'feed.xml',
        }
    ),
    (
        ('--input', '-i',),
        {
            "dest": 'input',
            "action": 'store',
            "type": str,
            "default": None,
            "help": 'relative path to file containing a list of files',
        }
    ),
    (
        ('--audible-cli-data',),
        {
            "dest": 'audible_cli_data',
            "action": 'store',
            "help": 'filename of library export from mkb79/audible-cli',
            "default": '',
        },
    ),
]

cmdline = configargparse.ArgumentParser()

for argument_commands, argument_options in ARGUMENTS:
    cmdline.add_argument(*argument_commands, **argument_options)

args = cmdline.parse_args(sys.argv[1:])
