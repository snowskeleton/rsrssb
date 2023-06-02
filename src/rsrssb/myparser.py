from ._version import __version__
import argparse
import sys



parser = argparse.ArgumentParser(description='You Need a Mint (YNAM)')
add = parser.add_argument

add('--domain', '-d',
    action='store',
    dest='domain',
    help='Base URL (e.g., example.net)',
    type=str,
    default='')
add('--date-from-timestamp',
    action='store_true',
    dest='date_from_timestamp',
    help='Use file timestamp instead of metadata timestamp')
add('--root', '-r',
    action='store',
    dest='root',
    help='The directory structor of your website before the podcast '
    '(path/to/files/) ',
    type=str,
    default='')
add('--title', '-t',
    action='store',
    dest='title',
    help='The name of your feed',
    type=str,
    default='')
add('--extension', '-e',
    action='store',
    dest='extensions',
    help='The format(s) of your audio files',
    type=str,
    nargs='*',
    default='mp3')
add('--output', '-o',
    action='store',
    dest='outputFile',
    help='Name of rss file to be created',
    type=str,
    default='feed.xml')
add('--input', '-i',
    action='store',
    dest='input',
    help='relative path to file containing a list of files (one per line)',
    type=str,
    default=None)
add('--audible-cli-data',
    action='store',
    dest='audible_cli_data',
    help='filename of library export from mkb79/audible-cli',
    type=str,
    default='')
add('--verbose', action='store_true', help='Enables console output')
add('--version',
    '-v',
    action='version',
    version='snowskeleton/rsrssb ' + __version__)

args, _ = parser.parse_known_args(sys.argv[1:])
