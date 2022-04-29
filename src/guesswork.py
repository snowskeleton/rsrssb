import os
import sys


# simple yes/no state determiner.
def approval(question) -> bool:
  match input(question + '(y/N)'):
    case 'y' | 'Y' | 'yes' | 'ye' | 'ys':
      return True
  return False

# returns list of all mp3 files in current directory,
# which is probably the files you're trying to make a
# pdocast feed from.
def guessFiles() -> list:
  return [f for f in os.listdir() if f.__contains__('.mp3')]