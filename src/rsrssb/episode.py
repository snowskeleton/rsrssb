from dataclasses import dataclass, field
from email.utils import format_datetime
from hashlib import sha256
import os
from datetime import datetime
from .tinytag import TinyTag
from typing import List


@dataclass
class Episode():
    filename: str
    description: str = field(init=False)
    title: str = field(init=False)
    bytes: str = field(init=False)
    pubDate: str = field(init=False)

    instances = []

    def __post_init__(self) -> None:
        tags = TinyTag.get(self.filename, encoding='MP4')
        self.title = _clean_title(tags.title)
        self.description = _choose_description(tags)

        # we want stable dates run-to-run, so we hash their title
        seed = _uniquifier(self.title)
        date = _puff_date(int(tags.year), seed)
        self.pubDate = format_datetime(date)

        if os.path.exists(self.filename):
            self.bytes = f'{os.path.getsize(self.filename)}'
        else:
            raise FileNotFoundError(self.filename)

        self.__class__.instances.append(self)

    # the following two functions proper sorting to be done on Episode objects
    def __lt__(self, other) -> bool:
        return self.title < other.title

    def __gt__(self, other) -> bool:
        return self.title > other.title


def _choose_description(tags: TinyTag) -> str:
    if 'description' in tags.extra.keys():
        des = tags.extra['description']
        des = des.encode('raw_unicode_escape')
        des = des.decode('unicode_escape')
        return des
    elif tags.description is not None:
        des = tags.description
        des = des.encode('raw_unicode_escape')
        des = des.decode('unicode_escape')
        return des
    else:
        return tags.comment


def _clean_title(title: str) -> str:
    return title.replace(' (Unabridged)', '')


def _puff_date(year: int, seed: int) -> datetime:
    month = (seed % 11) + 1  # one-indexed
    day = (seed % 27) + 1  # one-indexed
    hour = (seed % 23)  # zero-indexed
    minsec = (seed % 59)  # zero-indexed
    return datetime(
        year=year,
        minute=minsec,
        second=minsec,
        month=month,
        hour=hour,
        day=day,
    )


def _uniquifier(text: str) -> str:
    return int(sha256(text.encode()).hexdigest(), base=16)


def episodesFrom(files: list) -> List[Episode]:
    return [Episode(f) for f in files]
