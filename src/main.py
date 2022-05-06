#!/usr/bin/env python3
import os
from feed import Feed, Item
from xmlwriter import dothexml
from parser import parse
import sys


# simple yes/no state determiner.
def yesTo(question) -> bool:
	if parse.args.unattended:
		return True

	match input(question + '(y/N)'):
		case 'y' | 'Y' | 'yes' | 'ye' | 'ys':
			return True

	return False


# returns list of all mp3 files in current directory,
# which is probably the files you're trying to make a
# pdocast feed from.
def guessFiles(extension=parse.extension()) -> list:
	if parse.input != '':
		print(parse.input())
		with open(parse.input(), 'r') as file:
			a = file.readlines()
			return a

	return [f for f in os.listdir() if f.__contains__(extension)]


def main():
	try:
		files = guessFiles()
		done = False

		while not done:
			print('\n'.join(files))
			if yesTo('Are these the files you want to use? '):
				feed = Feed()
				for file in sorted(files):
					Item(file, parent=feed)

				with open(parse.output(), 'w') as output:
					output.write(dothexml(feed))

				done = True
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
