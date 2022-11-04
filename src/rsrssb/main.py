import sys
import os
from .feed import Feed, Episode
from .parser import args
from .xmlwriter import doTheXML


def main():
    if args.input is not None:
        with open(args.input, 'r') as source:
            files = source.readlines()
    else:
        files = [f for f in os.listdir() if f.__contains__(args.extension)]

    try:
        feed = Feed()
        files = Episode.populateFrom(files)
        with open(args.outputFile, 'w+') as output:
            output.write(doTheXML(feed, files))

    except KeyboardInterrupt:
        sys.exit(print('\nAbort mission.'))


if __name__ == '__main__':
    sys.exit(main())
