import json
import sys

from parser import parse
import re
import db


def tsv2json(input_file) -> list:
    arr = []
    file = open(input_file, 'r+')
    a = file.readline()

    # The first line consist of headings of the record
    # so we will store it in an array and move to
    # next line in input_file.
    headers = [t.strip() for t in a.split('\t')]
    for line in file:
        d = {}
        for t, f in zip(headers, line.split('\t')):

            # Convert each row into dictionary with keys as titles
            d[t] = f.strip()

        # we will use strip to remove '\n'.
        arr.append(d)

        # we will append all the individual dictionaires into list
        # and return as a hydrated json object
    return json.loads(json.dumps(arr))


def filterFiles():
    sortValue = parse.sort()
    fullLibrary = db._getAll()
    goodFiles = []

    # for now, only author sort is implemented.
    for book in fullLibrary:
        book['filePath'] = (book['title'] + ': ' +
                book['subtitle'] + '.mp3' if book['subtitle'] != '' else book['title'] + '.mp3')
        if authorsInList(book['authors'], sortValue):
            goodFiles += [book["filePath"]]
        # else:
        #     print(book['authors'], sortValue)
    return goodFiles


# changes ```any_filename.123``` to ```any_filename```
def stripFileExtension(fileName):
    return re.sub(r'\....$', '', fileName)


def authorsInList(authors, author):
    if type(authors) == type('some string'):
        if authors == author:
            return True

    for a in authors:
        if a == author:
            return True

    return False


def bookInSeries(book, series):
    return True if book.series_title == series else False
