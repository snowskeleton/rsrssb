import os
import re


class Feed():
    def __init__(self, title, domain):
        self.title: str = title
        self.root: str = os.path.abspath(self.title)
        self.domain: str = domain
        self.webmaster: str = 'webmaster@' + self.domain
        self.description: str = self.title

        # a magic regex that gets the parent dir without any preceding path
        dir = re.sub(r'^.*/', '', os.getcwd())
        self.link = f'https://{self.domain}/{dir}'
