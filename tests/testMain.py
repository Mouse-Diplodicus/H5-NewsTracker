import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import main
import feedparser


class TestMain(unittest.TestCase):

    mocked_pull_feed = MagicMock()
    mocked_build_library = MagicMock()

    # @patch('main.build_library()', mocked_build_library)
    # @patch('main.pull_feed()', mocked_pull_feed)
    def test_main(self):
        pass

    def test_cycle(self):
        pass

    def test_build_library(self):
        item = MagicMock()
        item.title = 'test title'
        item.link = 'http://www.testsite.com'
        feed = MagicMock()
        feed.entries = [item]
        library = main.build_library(feed)
        self.assertEqual(library[0][0], 'test title')
        self.assertEqual(library[0][1], 'http://www.testsite.com')

        

    def test_pull_feed(self):
        pass


if __name__ == "__main__":
    unittest.main()
