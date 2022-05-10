import json
from parser import parse
import re

def tsv2json(input_file) -> list:
    arr = []
    file = open(input_file, 'r')
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

def filterFiles(files):
    stuff = tsv2json(parse.audible_cli_data())
    val = parse.sort()
    goodFiles = []
    # don't reverse these for loops.
    # titles in library aren't guaranteed to be downloaded.
    for f in files:
        f = stripFileExtension(f)
        for s in stuff:
            if s['title'] == f:
                if val in str(s):
                    goodFiles.append(f)
    return goodFiles

def stripFileExtension(fileName):
    return re.sub(r'\....$', '', fileName)
