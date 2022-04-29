from fileinput import filename
import os
import re
from datetime import datetime

from template import ITEM_TEMPLATE, FOOTER
from templateEditor import header

class Feed():
  def __init__(self):
    self.title = input("Title: ")
    self.artwork = ''
    self.description = self.title
    self.link = input("Base URL (e.g., https://example.com): ")
    self.webmaster = input("Webmaster email: ")
    self.lastpubdate = input("Webmaster email: ")
    self.lastbuilddate = input("Webmaster email: ")

  def xml(self):
    feed = header(self)
    for item in Item.instances:
      feed += item.spaghetti()
    feed += FOOTER
    return feed


class Item():
  instances = []
  def __init__(self, fileName, parent) -> None:
      self.title = re.sub(r'.mp3|m4b|mb3|mb4', '', fileName)
      self.ep_link = f'{parent.link}/rss/{fileName}'
      self.enclosureURL = f'{parent.link}/rss/{fileName}'
      self.description = fileName
      self.bytes = f'{os.path.getsize(fileName)}'
      self.pubdate = f'{datetime.now()}'
      self.__class__.instances.append(self)

  def spaghetti(self) -> str:
    newItem = ITEM_TEMPLATE
    newItem = re.sub(';EP_TITLE', self.title, newItem)
    newItem = re.sub(';EP_LINK', self.ep_link, newItem)
    newItem = re.sub(';EP_DESCRIPTION', self.description, newItem)
    newItem = re.sub(';EP_ENCLOSURE_URL', self.enclosureURL, newItem)
    newItem = re.sub(';EP_LENGTH_IN_BYTES', self.bytes, newItem)
    newItem = re.sub(';EP_PUBDATE', self.pubdate, newItem)
    return newItem
