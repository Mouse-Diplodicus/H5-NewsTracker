"""Tests for main.py"""
import threading
import time
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from H5_News_Tracker.controller import main
from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestMain(unittest.TestCase):

    def test_build_news_ticker(self):
        """Testing the build_news_ticker function """
        with patch('H5_News_Tracker.parser.feed_interface.build_library') as mocked_build_library:
            with patch('H5_News_Tracker.parser.feed_interface.parse') as mocked_parser:
                with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
                    with patch('H5_News_Tracker.controller.main.threading.Thread') as mocked_thread:
                        main.build_news_ticker('https://news.google.com/news/rss')
                        mocked_build_library.assert_called_with(mocked_parser('https://news.google.com/news/rss'))
                        # mocked_ticker_window.assert_any_call()
                        # mocked_thread.assert_any_call()
                        mocked_ticker_window.assert_has_calls(mocked_ticker_window.start())

    def test_cycle(self):
        """
        Unit test for the cycle method
        When Cycle is run: it should call the update() function on the ticker it is passed after the Cycle_time
        has passed
        """
        mock_ticker = MagicMock()
        test_lib = [["headline_0", "https://test_0.com"], ["headline_1", "https://test_1.com"],
                    ["headline_2", "https://test_2.com"]]
        test_thread = threading.Thread(target=main.cycle, args=[mock_ticker, test_lib], name="Test-Cycle-Thread")

        try:
            # Act
            test_thread.start()

            # Assert
            time.sleep(main.CYCLE_TIME / 2)
            mock_ticker.update.assert_called_with(test_lib[0][0], test_lib[0][1])
            time.sleep(main.CYCLE_TIME)
            mock_ticker.update.assert_called_with(test_lib[1][0], test_lib[1][1])
            time.sleep(main.CYCLE_TIME)
            mock_ticker.update.assert_called_with(test_lib[2][0], test_lib[2][1])
        except AssertionError as err:
            raise err
        except BaseException as err:
            msg = "'cycle' command should not throw errors: " + repr(err)
            raise AssertionError(msg)

    def test_parse_args_default(self):
        parser = main.parse_args([])
        self.assertFalse(parser.url)

    def test_parse_args(self):
        parser = main.parse_args(['--url'])
        self.assertTrue(self, parser.url)
        parser = main.parse_args(['--file'])
        self.assertTrue(self, parser.file)
        parser = main.parse_args(['--config'])
        self.assertTrue(self, parser.config)

    def test_url_list_from_file(self):
        """
        Unit test for the url_list_from_file method
        """
        test_path = 'C:/Users/Mouse/Git/H5-NewsTracker/tests/urls.txt'
        test_result = main.url_list_from_file(test_path)
        expected_result = ['https://news.google.com/news/rss', 'http://rss.cnn.com/rss/cnn_topstories.rss',
                           'http://rss.cnn.com/rss/cnn_world.rss', 'https://www.reddit.com/.rss']
        self.assertEqual(expected_result, test_result)


if __name__ == '__main__':
    unittest.main()
