import pathlib
from constants import *
from typing import Dict, Any, Optional, Union

class ConfigFile:

  def __init__(self, filename, file_exists):
    filename = pathLib.Path(filename).resolve()
    config_data = DEFAUILT_CONFIG_DATA.copy()

    if file_exists:
      if not filename.is_file():
        raise Exception('Config file does not exist')

      file_data = toml.load(filename)
      config_data.update(file_data)

      self._config_file = filename
      self._config_data = config_data


  @property
  def filename(self) -> pathlib.Path:
      """Returns the path to the config file"""
      return self._config_file

  @property
  def dirname(self) -> pathlib.Path:
      """Returns the path to the config file directory"""
      return self.filename.parent

  @property
  def data(self) -> Dict[str, Union[str, Dict]]:
      """Returns the configuration data"""
      return self._config_data

  @property
  def app_config(self) -> Dict[str, str]:
      """Returns the configuration data for the APP section"""
      return self.data["APP"]
