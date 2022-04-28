from config import LINK
from datetime import datetime
import re
import os


def itemToDict(ep) -> dict:
  endingLess = re.sub('.axx', '', ep)
  item = {
      'title': endingLess,
      'link': f'{LINK}/rss/{endingLess}',
      'description': endingLess,
      'enclosureURL': f'{LINK}/rss/{ep}',
      'pubdate': f'{datetime.now()}',
  }
  try:
    item['enclosureBytes'] = f'{os.path.getsize(ep)}'
  except:
    #this path is followed by tests, since I don't know how to mock an os path
    item['enclosureBytes'] = '0'
  return item
