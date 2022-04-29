import unittest
from itemToDict import itemToDict
from hydrateItem import hydrateItem
from config import TITLE, LINK


class MyTestCases(unittest.TestCase):
    # this variable will be used several times thorughout this class
    test_file = 'this is a test string pretending to be a file'

    def test_itemToStr(self):
        test_obj = itemToDict(self.test_file)
        test_str = hydrateItem(test_obj)
        self.assertIn(
            '<title>this is a test string pretending to be a file</title>', test_str)
        # self.assertIn(
        # # <link>snowskeleton.net/rss/Magefall/01 Chapter 1</link>
        #     f'<link>{LINK}/rss/{TITLE}/this is a test string pretending to be a file</link>', test_str)

        # TODO: add tests for all of the commented lines below
        # <item>
        # <title>"01 Chapter 1"</title>
        # <link>snowskeleton.net/rss/Magefall/01 Chapter 1</link>
        # <description>"01 Chapter 1"</description>
        # <enclosure url="snowskeleton.net/rss/Magefall/01 Chapter 1.mp3" type="audio/mpeg" length="1289752"/>
        # <pubDate>"2022-04-28 23:36:59.207240"</pubDate>
        # </item>

    def test_dictToDict(self):
        test_obj = itemToDict(self.test_file)

        self.assertEqual(
            test_obj['title'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['link'], f'https://snowskeleton.net/rss/{TITLE}/this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['description'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test_obj['enclosureURL'], f'https://snowskeleton.net/rss/{TITLE}/this is a test string pretending to be a file')

        #this regex is supposed to matche a date formatted like so:
        # 'yyyy-MM-dd hh:mm:ss.ssssss', '2022-04-28 14:26:03.102815'
        self.assertRegex(
            test_obj['pubdate'],
            r'[0-9][0-9][0-9][0-9]' +
            r'-[0-9][0-9]-[0-9][0-9] ' +
            r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9]' +
            r'\.[0-9][0-9][0-9][0-9][0-9][0-9]'
        )


if __name__ == '__main__':
  unittest.main()
