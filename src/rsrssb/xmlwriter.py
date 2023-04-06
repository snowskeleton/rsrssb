from xml.dom import minidom
import urllib.parse
from urllib.parse import quote
from datetime import datetime


def doTheXML(feed, files):
    root = minidom.Document()

    # start creating the tree
    rss = root.createElement('rss')
    rss.setAttribute('version', '2.0')
    rss.setAttribute('xmlns:atom', 'http://www.w3.org/2005/Atom')
    rss.setAttribute(
        'xmlns:itunes', 'http://www.itunes.com/dtds/podcast-1.0.dtd')
    rss.setAttribute('xmlns:ituneu', 'http://www.itunesu.com/feed')
    channel = root.createElement('channel')
    smear(rss, channel)

    # define all the headers
    title = root.createElement('title')
    link = root.createElement('link')
    description = root.createElement('description')
    itblock = root.createElement('itunes:block')
    itimage = root.createElement('itunes:image')
    itimage.setAttribute('url', f'{feed.link}/cover.jpg')
    pubDate = root.createElement('lastpubdate')
    lastBuildDate = root.createElement('lastBuildDate')
    webmaster = root.createElement('webmaster')
    docs = root.createElement('docs')

    # smack 'em all together
    smush(title, feed.title)
    smush(link, feed.link)
    smush(description, feed.description)
    smush(webmaster, feed.webmaster)
    date = datetime.now().strftime('%Y-%m-%d')
    smush(pubDate, date)
    smush(lastBuildDate, date)
    smush(docs, 'http://blogs.law.harvard.edu/tech/rss')
    for tag in [title, link, description, webmaster,
                pubDate, lastBuildDate, docs, itblock, itimage]:
        smear(channel, tag)

    # time to create the items
    items = []
    easyFields = [
        'item',
        'title',
        'link',
        'description',
        'pubDate',
        'enclosure',
    ]
    for _item in sorted(files):
        for field in easyFields:
            field = root.createElement(f'{field}')
        item = root.createElement('item')
        title = root.createElement('title')
        link = root.createElement('link')
        description = root.createElement('description')
        pubDate = root.createElement('pubDate')
        enclosure = root.createElement('enclosure')
        enclosure.setAttribute('url', f'{feed.link}/{quote(_item.filename)}')
        enclosure.setAttribute('type', 'audio/mpeg')
        enclosure.setAttribute('length', f'{_item.bytes}')

        smush(title, f'{_item.title}')
        smush(link, f'{feed.link}/{_item.filename}')
        smush(description, f'{_item.description}')
        smush(pubDate, f'{_item.pubDate}')

        for tag in [title, link, description, pubDate, enclosure]:
            smear(item, tag)
            items.append(item)

    for tag in [*items]:
        smear(channel, tag)

    root.appendChild(rss)

    return root.toprettyxml(indent=' ')


def smush(tag, text):
    """
    <tag> text </tag>
    """
    tag.appendChild(minidom.Document().createTextNode(text))


def smear(tag, tig):
    """
    <tag> <tig> </tig> </tag>
    """
    tag.appendChild(tig)
