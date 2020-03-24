import unittest
from unittest.mock import patch
from H5_News_Tracker.parser import rss


class TestRss(unittest.TestCase):

    def test_parse_feed(self):
        with patch('H5_News_Tracker.parser.rss.parse_feed.feedparser.parse') as mocked_feed:
            mocked_feed.return_value = 'title'
            self.assertIsNotNone(rss.parse_feed())
