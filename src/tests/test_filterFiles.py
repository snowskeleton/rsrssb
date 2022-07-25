# import unittest
import unittest
from db import Book
from .longData import books
import os

class MyTestCases(unittest.TestCase):

  def test_the_thing(self):
    for book in books:
      self.assertEqual(book['title'], 1)

# from alchemy_mock.mocking import UnifiedAlchemyMagicMock
# db_session = UnifiedAlchemyMagicMock()

# mock_res = test_asd(db_session)
# self.assertEqual(mock_res, [1,2,3])

# from utils import filterFiles

# db_session.add(Book(column1=1, column2=2, column3=3))
# Book()



# class MyTestCases(unittest.TestCase)':

#   def
