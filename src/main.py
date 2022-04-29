#!/usr/bin/env python3
import sys
from itemToDict import itemToDict
from hydrateItem import hydrateItem
from config import *
from template import *
from removeVars import removeVars


def audioFileCheck(item):
	if item.__contains__(r'.*\.jpg|.*\.png|.*\.xml|rss'):
		return False
	return True

def out(string):
	print(string, file = sys.stdout)

def main():
	# if len(sys.argv) < 2:
	# 	print("Please supply audio files as arguments")
	# 	raise SystemExit

		# if audioFileCheck(arg) != False: # i.e., if the argument is a non-audio file
			# ARTWORK = arg
			# sys.argv.pop(arg)

	#add header to feed.xml. only need to do this once per file
	bt = removeVars(HEADER)
	out(bt)

	#work through all the audio files, making a listing for each.
	for i in sys.stdin:
		if audioFileCheck(i) == True:
			#convert string into dict
			som = itemToDict(i)

			#exchange dict for loooooong string
			som = hydrateItem(som)

			#write long string to file
			out(som)

	out(FOOTER)

if __name__ == '__main__':
	main()
