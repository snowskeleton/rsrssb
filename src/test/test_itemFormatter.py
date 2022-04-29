import unittest
from itemToDict import itemToDict
from hydrateItem import hydrateItem
from config import TITLE


class MyTestCases(unittest.TestCase):
    # this variable will be used several times thorughout this class
    test_file = 'this is a test string pretending to be a file'

    def test_itemToStr(self):
        test_obj = itemToDict(self.test_file)
        test_str = hydrateItem(test_obj)
        self.assertIn(
            '<title>"this is a test string pretending to be a file"</title>', test_str)

    def test_dictToDict(self):
        test_obj = itemToDict(self.test_file)

        self.assertEqual(
            test_obj['title'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['link'], f'snowskeleton.net/rss/{TITLE}/this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['description'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['enclosureURL'], f'snowskeleton.net/rss/{TITLE}/this is a test string pretending to be a file')

        #this regex is supposed to matche a date formatted like so:
        # 'yyyy-MM-dd hh:mm:ss.ssssss', '2022-04-28 14:26:03.102815'
        self.assertRegex(
            test_obj['pubdate'],
            '[0-9][0-9][0-9][0-9]' +
            '-[0-9][0-9]-[0-9][0-9] ' +
            '[0-9][0-9]:[0-9][0-9]:[0-9][0-9]' +
            '\.[0-9][0-9][0-9][0-9][0-9][0-9]'
        )


if __name__ == '__main__':
  unittest.main()
