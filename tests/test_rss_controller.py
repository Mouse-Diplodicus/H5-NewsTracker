"""Tests for rss_controller.py"""
import threading
import time
import tkinter
import unittest
import sys
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import rss_controller
from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.controller import utilities
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.parser.feed_interface import ThreadSafeList


class TestMain(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.library = ThreadSafeList()
        cls.library.append(["headline_0", "https://test_0.com"])
        cls.library.append(["headline_1", "https://test_1.com"])
        cls.library.append(["headline_2", "https://test_2.com"])
        cls.test_config = utilities.load_config_file()['ticker_window']

    @patch('H5_News_Tracker.controller.rss_controller.Controller')
    def test_start(self, mock_controller):
        print(sys.argv)
        sys.argv[1] = '-vvv'
        sys.argv[2] = '-t'
        sys.argv[3] = '5'
        sys.argv[4] = '-u'
        sys.argv.append('https://news.google.com/news/rss')
        sys.argv.append('-s')
        sys.argv.append('14')
        sys.argv.append('-c')
        sys.argv.append('black')
        sys.argv.append('-b')
        sys.argv.append('white')
        sys.argv.append('-l')
        sys.argv.append('path_to_nothing')
        rss_controller.start()
        self.assertTrue(mock_controller.called)
        mock_controller.assert_has_calls(mock_controller.start_gui())

    def test_url_list_from_file(self):
        """
        Unit test for the url_list_from_file method
        """
        test_result = rss_controller.url_list_from_file('urls.txt')
        if test_result is None:
            test_result = rss_controller.url_list_from_file('tests/urls.txt')

        expected_result = ['https://news.google.com/news/rss', 'http://rss.cnn.com/rss/cnn_topstories.rss',
                           'http://rss.cnn.com/rss/cnn_world.rss', 'https://www.reddit.com/.rss']
        self.assertEqual(expected_result, test_result)

    def test_build_library(self):
        with patch('H5_News_Tracker.parser.feed_interface.build_library') as mocked_build_library:
            with patch('H5_News_Tracker.parser.feed_interface.parse') as mocked_parser:
                rss_controller.build_library(['https://news.google.com/news/rss'])
                mocked_build_library.assert_called_with(mocked_parser('https://news.google.com/news/rss'))

    def test_parse_args(self):
        pass

    @patch("H5_News_Tracker.controller.rss_controller.Controller.cycle")
    def test_controller_init(self, mock_cycle):
        """Testing the build_news_ticker function """
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
            rss_controller.Controller(self.library, cycle_time=3, ticker_config=self.test_config)
            self.assertTrue(mock_cycle.called)
            mocked_ticker_window.assert_has_calls(mocked_ticker_window.start())

    @patch("H5_News_Tracker.gui.ticker_window.TickerWindow.update_headline")
    def test_cycle(self, mock_update_headline):
        """
        Unit test for the cycle method
        When Cycle is run: it should call the update() function on the ticker it is passed after the Cycle_time
        has passed
        """
        mock_ticker = MagicMock()
        test_lib = ThreadSafeList()
        test_lib.append(["headline_0", "https://test_0.com"])
        test_lib.append(["headline_1", "https://test_1.com"])
        test_lib.append(["headline_2", "https://test_2.com"])
        controller = rss_controller.Controller(test_lib, cycle_time=2, ticker_config=self.test_config)
        test_thread = threading.Thread(target=controller.cycle, args=[mock_ticker, self.library],
                                       kwargs=dict(iterations=2), name="Test-Cycle-Thread")
        try:
            # Act
            test_thread.start()
            # Assert
            time.sleep(controller.cycle_time / 2)
            self.assertTrue(mock_update_headline.called)
        except AssertionError as err:
            raise err
        except BaseException as err:
            msg = "'cycle' command should not throw errors: " + repr(err)
            raise AssertionError(msg)

    def test_start_gui(self):
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
            control = rss_controller.Controller(self.library, cycle_time=3, ticker_config=self.test_config)
            kill_thread = threading.Thread(target=control.ticker.close, args=[1], name="Test-Kill-Thread",
                                           daemon=True)
            kill_thread.start()
            control.start_gui()
            mocked_ticker_window.assert_has_calls(mocked_ticker_window.start())


if __name__ == '__main__':
    unittest.main()
