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

    mocked_feed = MagicMock()

    @patch('main.build_rss_ticker()', mocked_feed)
    def test_build_library(self, mocked_feed):
        mocked_feed()
        print(mocked_feed)

    def test_pull_feed(self):
        pass


if __name__ == "__main__":
    unittest.main()
