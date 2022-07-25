import unittest
from utils import stripFileExtension


class MyTestCases(unittest.TestCase):

  def test_stripMp3(self):
    fullFile = 'Words of Radiance: The Stormlight Archive, Book 2.mp3'
    strippedFile = 'Words of Radiance: The Stormlight Archive, Book 2'
    self.assertEqual(strippedFile, stripFileExtension(fullFile))

  def test_dontStripWithNoExtension(self):
    fullFile = 'Words of Radiance: The Stormlight Archive, Book 2'
    strippedFile = 'Words of Radiance: The Stormlight Archive, Book 2'
    self.assertEqual(strippedFile, stripFileExtension(fullFile))
