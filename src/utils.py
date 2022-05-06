import json

def tsv2json(_, input_file) -> list:
    arr = []
    file = open(input_file, 'r')
    a = file.readline()

    # The first line consist of headings of the record
    # so we will store it in an array and move to
    # next line in input_file.
    titles = [t.strip() for t in a.split('\t')]
    for line in file:
        d = {}
        for t, f in zip(titles, line.split('\t')):

            # Convert each row into dictionary with keys as titles
            d[t] = f.strip()

        # we will use strip to remove '\n'.
        arr.append(d)

        # we will append all the individual dictionaires into list
        # and return as a hydrated json object
    return json.loads(json.dumps(arr))
