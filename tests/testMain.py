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
        with patch('H5_News_Tracker.controller.main.build_rss_ticker') as mocked_ticker:
            mocked_ticker.return_value = 'ticker'
            self.assertIsNotNone(main.build_rss_ticker())

    def test_cycle(self):
        pass

    def test_build_library(self):
        item = MagicMock()
        item.title = 'test title'
        item.link = 'http://www.testsite.com'
        item_empty = MagicMock()
        item_empty.title = ''
        item_empty.link = ''
        item_none = MagicMock()
        item_none.title = None
        item_none.link = None
        feed = MagicMock()

        feed.entries = [item]
        feed.entries.append(item_empty)
        feed.entries.append(item_none)
        library = main.build_library(feed)
        self.assertEqual(library[0][0], 'test title')
        self.assertEqual(library[0][1], 'http://www.testsite.com')
        self.assertEqual(library[1][0], '')
        self.assertEqual(library[1][1], '')
        self.assertEqual(library[2][0], None)
        self.assertEqual(library[2][1], None)

    def test_pull_feed(self):
        pass


if __name__ == "__main__":
    unittest.main()
