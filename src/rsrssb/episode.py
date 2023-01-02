from dataclasses import dataclass, field
from email.utils import format_datetime
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

    def populatedFrom(files):
        return [Episode(f) for f in files]

    def __post_init__(self) -> None:
        tags = TinyTag.get(self.filename, encoding='MP4')
        self.title = tags.title.replace(' (Unabridged)', '')
        if 'description' in tags.extra.keys():
            des = tags.extra['description']
            des = des.encode('raw_unicode_escape')
            des = des.decode('unicode_escape')
            des = des if des is not None else self.title
            self.description = des
        else:
            des = tags.comment if tags.comment is not None else self.title
            self.description = des

        t = datetime.now().replace(year=int(tags.year))
        t -= timedelta(days=len(self.instances))
        self.pubDate = format_datetime(t)

        # file size in bytes (required for podcast feed)
        if os.path.exists(self.filename):
            self.bytes = f'{os.path.getsize(self.filename)}'
        else:
            raise (FileNotFoundError(self.filename))

        self.__class__.instances.append(self)

    # the following two functions proper sorting to be done on Episode objects
    def __lt__(self, other):
        return self.title < other.title

    def __gt__(self, other):
        return self.title > other.title
