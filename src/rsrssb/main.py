import sys
import os
from .feed import Feed
from .episode import episodesFrom
from .myparser import args
from .xmlwriter import doTheXML


def main():
    title, domain = args.title, args.domain
    feed = Feed(title, domain)
    files = episodesFrom(derivedFiles())
    with open(args.outputFile, 'w+') as output:
        textfeed = doTheXML(feed, files)
        output.write(textfeed)


def other_main(title, domain, file_location, feed_file):
    feed = Feed(title, domain)
    files = episodesFrom(files)
    with open(feed_file, 'w+') as output:
        textfeed = doTheXML(feed, files)
        output.write(textfeed)

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
