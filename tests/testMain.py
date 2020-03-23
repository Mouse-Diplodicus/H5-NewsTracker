import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import main
import testFeed


class TestMain(unittest.TestCase):

    def test_main(self):
        pass

    def test_cycle(self):
        pass

    mocked_feed = MagicMock()

    @patch('feedparser.parse()', mocked_feed)
    def test_build_library(self, mocked_feed):
        print(mocked_feed)


    def test_pull_feed(self):
        pass
