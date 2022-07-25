import pathlib
import json, toml
import utils
import os, sys



configFile = os.path.expanduser('~') + '/.rsrssb/config.toml'
configData = toml.load(configFile)

WEBSITE_ROOT = configData['APP']['root']

DEFAULT_CONFIG_DATA = {
    "title": "RSRSSB Config File",
    "APP": {},
}
