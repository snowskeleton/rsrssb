import unittest
from unittest import mock

from constants import *


class MyTestCases(unittest.TestCase):

  @mock.patch('constants.toml.load', return_value={'title': 'RSRSSB Config File', 'APP': {'root': 'this is some dir value'}})
  def test_website_root(self, mock_toml_load):
    # mock_configData = {'title': 'RSRSSB Config File', 'APP': {'root': 'this is some dir value'}}
    self.assertEqual(WEBSITE_ROOT, 'this is some dir value')
