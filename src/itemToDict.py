from config import LINK, TITLE
from datetime import datetime
import re
import os


def itemToDict(ep) -> dict:
  # TODO: test this
  endingLess = re.sub(r'.mp3|m4b|mb3|mb4', '', ep)

  item = {
      'title': endingLess,
      'link': f'{LINK}/rss/{TITLE}/{endingLess}',
      'description': endingLess,
      'enclosureURL': f'{LINK}/rss/{TITLE}/{ep}',
      'pubdate': f'{datetime.now()}',
  }
  try:
    item['enclosureBytes'] = f'{os.path.getsize(ep)}'
  except:
    #this path is followed by tests, since I don't know how to mock an os path
    item['enclosureBytes'] = '0'
  return item

if __name__ == '__main__':
  itemToDict()
