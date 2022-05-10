import os
import re
from datetime import datetime, timedelta

from variables import env
from parser import parse
from utils import stripFileExtension, tsv2json


class Feed():
  def __init__(self):
    self.title = env.title()
    self.root = os.path.abspath(self.title)
    self.description = self.title
    self.domain = env.domain()
    self.webmaster = 'webmaster@' + self.domain
    self.lastpubdate = f'{datetime.now()}'
    self.lastbuilddate = f'{datetime.now()}'

    # a magic regex that gets the parent dir without any preceding path
    dir = re.sub(r'^.*/', '', os.getcwd())
    self.link = f'https://{self.domain}/rss/{dir}'


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

  # yay abstraction
  def description(self):
    try:
      return self.ac_description
    except:
      return self._description

  def pubDate(self):
    try:
      return self.ac_pub_date
    except:
      return self._pubDate

  def __init__(self, fileName, parent) -> None:
      # changes ```any_filename.123``` to ```any_filename```
      self.title = stripFileExtension(fileName)
      self._description = self.title

      # if we have the audible-cli data, use it
      if parse.audible_cli_data() != '':
        data = tsv2json(parse.audible_cli_data())
        for book in [b for b in data if b['title'] in self.title]:
          self.ac_description = book['description']
          self.ac_series_title = book['series_title']
          self.ac_series_sequence = book['series_sequence']
          self.ac_subtitle = book['subtitle']
          self.ac_release_date = book['release_date']
          self.ac = True

      self.ep_link = f'{parent.link}/{fileName}'
      self.enclosureURL = self.ep_link

      # file size in bytes (required for podcast feed)
      self.bytes = f'{os.path.getsize(fileName)}'

      # this date increases by one day for each item that has so far been created.
      self._pubDate = f'{(datetime.now() - timedelta(days=len(self.instances())))}'

      # add self to list of class items
      self.__class__._instances.append(self)
