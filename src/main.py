#!/usr/bin/env python3
import os
from feed import Feed, Item
from xmlwriter import dothexml
from parser import parse
import sys
from utils import filterFiles
import db


# simple yes/no state determiner.
def yesTo(question) -> bool:
	if parse.args.unattended:
		return True

	match input(question + '(y/N)'):
		case 'y' | 'Y' | 'yes' | 'ye' | 'ys':
			return True
		case 'q':
			sys.exit()

	return False


# returns list of all mp3 files in current directory,
# which is probably the files you're trying to make a
# pdocast feed from.
def guessFiles(extension=parse.extension()) -> list:
	i = parse.input()
	if i != '':
		with open(i, 'r') as file:
			a = file.readlines()
			return a

	files = [f for f in os.listdir() if f.__contains__(extension)]

	# checks if 'sort by author' flag is True
	if parse.sort():
		files = filterFiles()

	# print(files)
	# sys.exit()
	return files


def main():
	if parse.rebase():
		db.rebuildLibrary()
		sys.exit()
	try:
		files = guessFiles()
		done = False

		while not done:
			if not parse.silent():
				print('\n'.join(files))
			if yesTo('Are these the files you want to use? '):
				feed = Feed()
				# print(files)
				# sys.exit()
				for file in sorted(files):
					Item(file, parent=feed)

				with open(parse.output(), 'w') as output:
					output.write(dothexml(feed))

				done = True
				if not parse.silent():
					print('Done')
				sys.exit()

			else:
				longstring = "Type an extension (e.g., mp3, m4b, aac): "
				files = guessFiles(input(longstring))

	except KeyboardInterrupt:
		print('\nAbort mission.')
		sys.exit()


if __name__ == '__main__':
	main()
