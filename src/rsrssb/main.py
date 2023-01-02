import sys
import os
from .feed import Feed, Episode
from .myparser import args
from .xmlwriter import doTheXML


def main():
    if args.input is not None:
        with open(args.input, 'r') as source:
            files = source.readlines()
    else:
        files = [f for f in os.listdir() if f.__contains__(args.extension)]

    feed = Feed()
    files = Episode.populateFrom(files)
    with open(args.outputFile, 'w+') as output:
        output.write(doTheXML(feed, files))


if __name__ == '__main__':
    sys.exit(main())
