import re
from turtle import right
from template import ITEM_TEMPLATE
from variables import *
import re


def hydrateItem(item):
    newItem = ITEM_TEMPLATE
    newItem = re.sub(';EP_TITLE', item['title'], newItem)
    newItem = re.sub(';EP_LINK', item['link'], newItem)
    newItem = re.sub(';EP_DESCRIPTION', item['description'], newItem)
    newItem = re.sub(';EP_ENCLOSURE_URL', item['enclosureURL'], newItem)
    newItem = re.sub(';EP_LENGTH_IN_BYTES', item['enclosureBytes'], newItem)
    newItem = re.sub(';EP_PUBDATE', item['pubdate'], newItem)
    return newItem
