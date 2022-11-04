from dataclasses import dataclass, field
import os
import re
from datetime import datetime, timedelta
from tinytag import TinyTag

from .parser import args


class Feed():
    def __init__(self):
        self.title = args.title
        self.root = os.path.abspath(self.title)
        self.description = self.title
        self.domain = args.domain
        self.webmaster = 'webmaster@' + self.domain
        self.lastpubdate = f'{datetime.now()}'
        self.lastbuilddate = f'{datetime.now()}'

        # a magic regex that gets the parent dir without any preceding path
        dir = re.sub(r'^.*/', '', os.getcwd())
        self.link = f'https://{self.domain}/rss/{dir}'


@dataclass
class Episode():
    filename: str
    description: str = field(init=False)
    title: str = field(init=False)
    bytes: str = field(init=False)
    pubDate: str = field(init=False)

    instances = []

    def populateFrom(files):
        return [Episode(f) for f in files]

    def __post_init__(self) -> None:
        tags = TinyTag.get(self.filename, encoding='MP4')
        self.title = tags.title.replace(' (Unabridged)', '')
        self.description = tags.comment
        t = datetime.now().replace(year=int(tags.year))
        t -= timedelta(days=len(self.instances))
        self.pubDate = f"{t.strftime('%Y-%m-%d')}"
        self.__class__.instances.append(self)

        # file size in bytes (required for podcast feed)
        try:
            self.bytes = f'{os.path.getsize(self.filename)}'
        except:
            # this exception is usually caused by testing RSRSSB with incorrect filenames.
            print(f'Incorrect filename: {self.filename}')
            self.bytes = '0'

    # the following two functions proper sorting to be done on Episode objects
    def __lt__(self, other):
        return self.title < other.title

    def __gt__(self, other):
        return self.title > other.title
