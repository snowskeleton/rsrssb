import sys
import os
from .feed import Feed
from .episode import Episode
from .myparser import args
from .xmlwriter import doTheXML


def main():
    feed = Feed()
    files = Episode.populatedFrom(derivedFiles())
    with open(args.outputFile, 'w+') as output:
        output.write(doTheXML(feed, files))


def derivedFiles() -> list:
    if args.input is not None:
        with open(args.input, 'r') as source:
            return source.readlines()

    exts = args.extensions
    potentialFiles = os.listdir()
    files = []

    for file in potentialFiles:
        ext = os.path.splitext(file)[-1].lower()
        if ext in exts or ext.replace('.', '') in exts:
            files.append(file)

    return files


if __name__ == '__main__':
    sys.exit(main())
