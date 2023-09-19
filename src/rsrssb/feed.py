import os
import re


class Feed():
    def __init__(self, title, domain):
        self.title: str = title
        self.root: str = os.path.abspath(self.title)
        self.domain: str = domain
        self.webmaster: str = 'webmaster@' + re.sub(r'/.*$', '', self.domain)
        self.description: str = self.title

        # a magic regex that gets the parent dir without any preceding path
        self.link = f'https://{self.domain}'
