import os


# simple yes/no state determiner.
def yesTo(question) -> bool:
  match input(question + '(y/N)'):
    case 'y' | 'Y' | 'yes' | 'ye' | 'ys':
      return True
  return False

# returns list of all mp3 files in current directory,
# which is probably the files you're trying to make a
# pdocast feed from.
def guessFiles(extension = 'mp3') -> list:
  return [f for f in os.listdir() if f.__contains__(extension)]
