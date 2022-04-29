import re
from config import *
from template import HEADER


def removeVars(template):
  template = re.sub(r";TITLE", f'{TITLE}', template)
  template = re.sub(r";DESCRIPTION", f'{DESCRIPTION}', template)
  template = re.sub(r";LINK", f'{LINK}', template)
  template = re.sub(r";LASTBUILDDATE", f'{LASTBUILDDATE}', template)
  template = re.sub(r";LASTPUBDATE", f'{LASTPUBDATE}', template)
  template = re.sub(r";WEBMASTER", f'{WEBMASTER}', template)
  return template

if __name__ == '__main__':
  removeVars(HEADER)
