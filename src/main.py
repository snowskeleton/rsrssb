#!/usr/bin/env python3
import os
from feed import Feed, Item
from xmlwriter import dothexml


# simple yes/no state determiner.
def yesTo(question) -> bool:
  match input(question + '(y/N)'):
    case 'y' | 'Y' | 'yes' | 'ye' | 'ys':
      return True
  return False

# returns list of all mp3 files in current directory,
# which is probably the files you're trying to make a
# pdocast feed from.


def guessFiles(extension='mp3') -> list:
  return [f for f in os.listdir() if f.__contains__(extension)]


def persistinator(files):
	feed = Feed()
	for file in sorted(files):
		Item(file, parent=feed)
	with open('feed.xml', 'w') as output:
		output.write(dothexml(feed))


def main():
	ext = guessFiles()
	done = False

	while not done:
		print('\n'.join(ext))
		if yesTo('Are these the files you want to use? '):
			persistinator(ext)
			done = True
			print('Done')
		else:
			longstring = "Type an extension (e.g., mp3, m4b, aac): "
			ext = guessFiles(input(longstring))
		# ext =
		# try removing the line break and having vscode autoformat for you


if __name__ == '__main__':
	main()
