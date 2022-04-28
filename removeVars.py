import re
from variables import *


def removeVars(template):
  template = re.sub(r";TITLE", f'{TITLE}', template)
  template = re.sub(r";DESCRIPTION", f'{DESCRIPTION}', template)
  template = re.sub(r";LINK", f'{LINK}', template)
  template = re.sub(r";LASTBUILDDATE", f'{LASTBUILDDATE}', template)
  template = re.sub(r";LASTPUBDATE", f'{LASTPUBDATE}', template)
  template = re.sub(r";WEBMASTER", f'{WEBMASTER}', template)
  return template
