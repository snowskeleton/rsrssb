#!/usr/bin/env python3
from template import *
from guesswork import approval, guessFiles
from feed import Feed, Item


def main():
	ext = guessFiles()
	found = False

	while not found:
		print('\n'.join(ext))
		if yesTo('Are these the files you want to use? '):
			horse(ext)
			found = True
		else:
			ext = guessFiles(
				input("Type which extension you're using (e.g., mp3, m4b, aac): "))

	print('Done')


def horse(files):
	feed = Feed()
	with open('feed.xml', 'w') as output:
		for f in sorted(files):
			Item(f, parent=feed)
		output.write(str(feed.xml()))


if __name__ == '__main__':
	main()
