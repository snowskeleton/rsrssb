import os
import re
from datetime import datetime, timedelta

from variables import env


class Feed():
  def __init__(self):
    self.title = env.title()
    self.root = os.path.abspath(self.title)
    self.description = self.title
    self.domain = env.domain()
    self.webmaster = 'webmaster@' + self.domain
    self.lastpubdate = f'{datetime.now()}'
    self.lastbuilddate = f'{datetime.now()}'

    # hafta do some string sanitization
    cleanTitle = re.sub(' ', '', self.title)

    # a magic regex that gets the parent dir without any preceding path
    a = re.sub(r'^.*/', '', os.path.dirname(os.getcwd()))

    self.link = f'https://{self.domain}/rss/{a}/{cleanTitle}'


class Item():
  _instances = []

  @classmethod
  def instances(self):
    return sorted(self._instances)

  # the following two functions proper sorting to be done on Item objects
  def __lt__(self, other):
    return self.title < other.title

  def __gt__(self, other):
    return self.title > other.title

  def __init__(self, fileName, parent) -> None:
      self.title = re.sub(r'.mp3|.m4b|.mb3|.mb4|.m4a', '', fileName)
      self.ep_link = f'{parent.link}/{fileName}'
      self.enclosureURL = self.ep_link
      self.description = fileName
      # file size in bytes (required for podcast feed)
      self.bytes = f'{os.path.getsize(fileName)}'
      # this date increases by one day for each item that has so far been created.
      self.pubDate = f'{(datetime.now() - timedelta(days=len(self.instances())))}'
      # add self to list of class items
      self.__class__._instances.append(self)
