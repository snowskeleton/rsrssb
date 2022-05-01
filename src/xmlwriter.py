from xml.dom import minidom
from feed import Item
from datetime import datetime


# <tag> text </tag>
def smush(tag, text):
  tag.appendChild(minidom.Document().createTextNode(text))

# <tag> <tig> </tig> </tag>
def smear(tag, tig):
  tag.appendChild(tig)

def dothexml(feed):
  root = minidom.Document()

  # start creating the tree
  rss = root.createElement('rss')
  channel = root.createElement('channel')
  smear(rss, channel)

  # define all the headers
  title = root.createElement('title')
  link = root.createElement('link')
  description = root.createElement('descritpion')
  webmaster = root.createElement('webmaster')
  pubDate = root.createElement('lastpubdate')
  lastBuildDate = root.createElement('lastBuildDate')
  docs = root.createElement('docs')

  #smack 'em all together
  smush(title, f'{feed.title}')
  smush(link, f'{feed.domain}')
  smush(description, f'{feed.description}')
  smush(webmaster, f'{feed.webmaster}')
  smush(pubDate, f'{datetime.now()}')
  smush(lastBuildDate, f'{datetime.now()}')
  smush(docs, 'http://blogs.law.harvard.edu/tech/rss')
  for tag in [title, link, description, webmaster,
              pubDate, lastBuildDate, docs]:
    smear(channel, tag)

  # time to create the items
  items = []
  for item in Item.instances():
    _item = root.createElement('item')
    title = root.createElement('title')
    link = root.createElement('link')
    description = root.createElement('descritpion')
    pubDate = root.createElement('pubDate')
    enclosure = root.createElement('enclosure')
    enclosure.setAttribute('url', f'{item.ep_link}')
    enclosure.setAttribute('type', 'audio/mpeg')
    enclosure.setAttribute('length', f'{item.bytes}')

    smush(title, f'{item.title}')
    smush(link, f'{item.enclosureURL}')
    smush(description, f'{item.description}')
    smush(pubDate, f'{item.pubDate}')

    for tag in [title, link, description, pubDate, enclosure]:
      smear(_item, tag)
      items.append(_item)

  for tag in [*items]:
    smear(channel, tag)

  root.appendChild(rss)

  return root.toprettyxml(indent=' ')
