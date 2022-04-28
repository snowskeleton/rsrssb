import unittest
from ..itemToDict import itemToDict
from itemFormatter import hydrateItem


class MyTestCases(unittest.TestCase):
    test__file = 'this is a test string pretending to be a file'
    # test__obj = epToDict(test__file)
    # test__str = hydrateItem(test__obj)

    def test__itemToStr(self):
        test__obj = itemToDict(self.test__file)
        test__str = hydrateItem(test__obj)
        self.assertIn(
            '<title>"this is a test string pretending to be a file"</title>', test__str)

    def test__dictToDict(self):
        test__obj = itemToDict(self.test__file)

        self.assertEqual(
            test__obj['title'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test__obj['link'], 'snowskeleton.net/rss/this is a test string pretending to be a file')
        self.assertEqual(
            test__obj['description'], 'this is a test string pretending to be a file')
        self.assertEqual(
            test__obj['enclosureURL'], 'snowskeleton.net/rss/this is a test string pretending to be a file')

        #this regex is supposed to matche a date formatted like so:
        # 'yyyy-MM-dd hh:mm:ss.ssssss', '2022-04-28 14:26:03.102815'
        self.assertRegex(
            test__obj['pubdate'],
            '[0-9][0-9][0-9][0-9]' +
            '-[0-9][0-9]-[0-9][0-9] ' +
            '[0-9][0-9]:[0-9][0-9]:[0-9][0-9]' +
            '\.[0-9][0-9][0-9][0-9][0-9][0-9]'
        )

    def test__noSpacesInLinks(self):
        test__obj = itemToDict(self.test__file)

        self.assertNotIn(' ', test__obj['link'])
        self.assertNotIn(' ', test__obj['enclosureURL'])


if __name__ == '__main__':
  unittest.main()
