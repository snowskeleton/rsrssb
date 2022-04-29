import sys
from itemToDict.itemToDict import itemToDict
from hydrateItem import hydrateItem
from config import *
from template import *
from removeVars import removeVars


def main():
	if len(sys.argv) < 2:
		print("Please supply audio files as arguments")
		raise SystemExit


	with open('feed.xml', 'w') as output:
		#add header to feed.xml. only need to do this once per file
		bt = removeVars(HEADER)
		output.write(bt)

  	#remove script name from arguments, leaving just audio file names
		sys.argv.pop(0)

		#work through all the audio files, making a listing for each.
		for i in sys.argv:
			#convert string into dict
			som = itemToDict(i)

			#exchange dict for loooooong string
			som = hydrateItem(som)

			#write long string to file
			output.write(som)

		output.write(FOOTER)

if __name__ == '__main__':
	main()
