"""Tests for main.py"""
import unittest
import os
from H5_News_Tracker.controller import utilities


class TestMain(unittest.TestCase):
    """Testing class for Unit test for H5_News_tracker.controller.utilities"""

    def test_get_logger(self):
        """Unit test for H5_News_tracker.controller.utilities.get_logger"""
        logger = utilities.get_logger()

    def test_load_config_file(self):
        """Unit test for H5_News_tracker.controller.utilities.load_config_file"""
        os.remove('config.yml')
        test_config = utilities.load_config_file()
        self.assertEqual('black', test_config['ticker_window']['background_color'])
        self.assertEqual('white', test_config['ticker_window']['text_color'])
        self.assertEqual(12, test_config['ticker_window']['font_size'])
        self.assertEqual(6, test_config['source']['cycle_time'])
        self.assertEqual('https://news.google.com/news/rss', test_config['source']['default_url'])
        self.assertEqual(None, test_config['source']['path_to_file'])


if __name__ == '__main__':
        unittest.main()
