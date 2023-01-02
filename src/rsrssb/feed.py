import os
import re
from datetime import datetime

from .myparser import args


class Feed():
    def __init__(self):
        self.title = args.title
        self.root = os.path.abspath(self.title)
        self.description = self.title
        self.domain = args.domain
        self.webmaster = 'webmaster@' + self.domain
        self.date = f"{datetime.now().strftime('%Y-%m-%d')}"

        # a magic regex that gets the parent dir without any preceding path
        dir = re.sub(r'^.*/', '', os.getcwd())
        self.link = f'https://{self.domain}/rss/{dir}'
