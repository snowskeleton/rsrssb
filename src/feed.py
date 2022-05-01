from distutils.command.clean import clean
import os
import re
from datetime import datetime, timedelta

from input import Input


class Feed():
  def __init__(self):
    self.title = Input.title()
    self.description = self.title
    cleanTitle = re.sub(' ', '', self.title)
    self.link = f'https://{Input.link()}/rss/{cleanTitle}'
    self.webmaster = 'webmaster@' + self.link
    self.lastpubdate = f'{datetime.now()}'
    self.lastbuilddate = f'{datetime.now()}'


class Item():
  _instances = []
  @classmethod
  def instances(self):
    return sorted(self._instances)

  # the following two functions are defined so that proper sorting
  # can be done on Item objects
  def __lt__(self, other):
    return self.title < other.title
  def __gt__(self, other):
    return self.title > other.title

  def __init__(self, fileName, parent) -> None:
      self.title = re.sub(r'.mp3|.m4b|.mb3|.mb4|.m4a', '', fileName)
      self.ep_link = f'{parent.link}/{fileName}'
      self.enclosureURL = f'{parent.link}/{fileName}'
      self.description = fileName
      self.bytes = f'{os.path.getsize(fileName)}'
      # this date increases by one day for every item that has been created so far.
      self.pubDate = f'{(datetime.now() + timedelta(days=len(self.instances())))}'
      self.__class__._instances.append(self)
