#!/usr/bin/env python3
from template import *
from guesswork import approval, guessFiles
from feed import Feed, Item


def main():
	match input("Enter 'd' for deafult options: "):
		case "d" | "default" | _:
			print('\n'.join(guessFiles()))
			if approval('Are these the files you want to use? '):
				horse(guessFiles())
			else:
				ext = input("Type which extension you're using (e.g., mp3, m4b, aac): ")
				horse(guessFiles(ext))



def audioFileCheck(item):
	if item.__contains__(r'.*\.jpg|.*\.png|.*\.xml|rss'):
		return False
	return True


def horse(files):
	feed = Feed()
	with open('feed.xml', 'w') as output:
		for f in files:
			Item(f, parent=feed)
		output.write(str(feed.xml()))


if __name__ == '__main__':
	main()
