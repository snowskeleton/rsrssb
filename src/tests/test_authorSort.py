import unittest

from utils import authorsInList


class MyTestCases(unittest.TestCase):

  def test_oneAuthorInList(self):
    author = 'Brandon Sanderson'
    authors = ['Brandon Sanderson']
    self.assertTrue(authorsInList(authors, author))

  def test_moreThanOneAuthorInList(self):
    author = 'Brandon Sanderson'
    authors = ['Brandon Sanderson', 'Patrick Rothfuss']
    self.assertTrue(authorsInList(authors, author))

  def test_oneAuthorNotInList(self):
    author = 'Brandon Sanderson'
    authors = ['Patrick Rothfuss']
    self.assertFalse(authorsInList(authors, author))

  def test_moreThanOneAuthorNotInList(self):
    author = 'Brandon Sanderson'
    authors = ['Arkady Martine', 'Patrick Rothfuss']
    self.assertFalse(authorsInList(authors, author))

  def test_stringNotDict(self):
    author = 'Brandon Sanderson'
    authors = 'Brandon Sanderson'
    self.assertTrue(authorsInList(authors, author))
