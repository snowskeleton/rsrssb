import re
from template import HEADER


def header(feed):
  stringyFeed = HEADER
  stringyFeed = re.sub(r";LINK", f'{feed.link}', stringyFeed)
  stringyFeed = re.sub(r";TITLE", f'{feed.title}', stringyFeed)
  stringyFeed = re.sub(r";SQUISHTITLE", f'{feed.linkTitle}', stringyFeed)
  stringyFeed = re.sub(r";WEBMASTER", f'{feed.webmaster}', stringyFeed)
  stringyFeed = re.sub(r";DESCRIPTION", f'{feed.description}', stringyFeed)
  stringyFeed = re.sub(r";LASTPUBDATE", f'{feed.lastpubdate}', stringyFeed)
  stringyFeed = re.sub(r";LASTBUILDDATE", f'{feed.lastbuilddate}', stringyFeed)
  return stringyFeed
