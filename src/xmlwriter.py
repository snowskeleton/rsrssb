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
  rss.setAttribute('version', '2.0')
  rss.setAttribute('xmlns:atom', 'http://www.w3.org/2005/Atom')
  rss.setAttribute('xmlns:itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd')
  rss.setAttribute('xmlns:ituneu', 'http://www.itunesu.com/feed')
  channel = root.createElement('channel')
  smear(rss, channel)

  # define all the headers
  title = root.createElement('title')
  link = root.createElement('link')
  description = root.createElement('descritpion')
  itblock = root.createElement('itunes:block')
  itimage = root.createElement('itunes:image')
  itimage.setAttribute('url', f'{feed.link}/cover.jpg')
  pubDate = root.createElement('lastpubdate')
  lastBuildDate = root.createElement('lastBuildDate')
  webmaster = root.createElement('webmaster')
  docs = root.createElement('docs')

  #smack 'em all together
  smush(title, feed.title)
  smush(link, feed.link)
  smush(description, feed.description)
  smush(webmaster, feed.webmaster)
  smush(pubDate, str(datetime.now()))
  smush(lastBuildDate, str(datetime.now()))
  smush(docs, 'http://blogs.law.harvard.edu/tech/rss')
  for tag in [title, link, description, webmaster,
              pubDate, lastBuildDate, docs, itblock, itimage]:
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
