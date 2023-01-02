from dataclasses import dataclass, field
import os
from datetime import datetime, timedelta
from .tinytag import TinyTag


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
        if 'description' in tags.extra.keys():
            des = tags.extra['description']
            des = des.encode('raw_unicode_escape')
            des = des.decode('unicode_escape')
            des = des if des != None else self.title
            self.description = des
        else:
            self.description = tags.comment
        t = datetime.now().replace(year=int(tags.year))
        t -= timedelta(days=len(self.instances))
        self.pubDate = f"{t.strftime('%Y-%m-%d')}"
        self.__class__.instances.append(self)

        # file size in bytes (required for podcast feed)
        if os.path.exists(self.filename):
            self.bytes = f'{os.path.getsize(self.filename)}'
        else:
            print(f'Unable to locate file: {self.filename}')
            self.bytes = '0'

    # the following two functions proper sorting to be done on Episode objects
    def __lt__(self, other):
        return self.title < other.title

    def __gt__(self, other):
        return self.title > other.title
