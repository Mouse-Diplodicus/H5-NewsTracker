"""Tests for main.py"""
import unittest
import threading
import time
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import main
from H5_News_Tracker.gui import ticker_window


class TestMain(unittest.TestCase):

    def test_build_rss_ticker(self):
        """Testing the build_rss_ticker function """
        with patch('H5_News_Tracker.controller.main.pull_feed') as mocked_pull_feed:
            with patch('H5_News_Tracker.controller.main.build_library') as mocked_build_library:
                with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
                    with patch('H5_News_Tracker.controller.main.threading.Thread') as mocked_thread:
                        main.build_rss_ticker()
                        mocked_pull_feed.assert_called_with('https://news.google.com/news/rss')
                        mocked_build_library.assert_called_with(mocked_pull_feed('https://news.google.com/news/rss'))
                        mocked_ticker_window.assert_any_call()
                        # mocked_thread.assert_any_call()
                        mocked_ticker_window.assert_has_calls(ticker_window.TickerWindow.start())

    def test_build_library(self):
        """Testing the build_library function"""
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
        """Test the pull_feed function"""
        ssl = MagicMock()
        ssl._create_default_https_context = 'fake url'
        feed_url = ssl._create_default_https_context
        main.pull_feed(feed_url)
        self.assertEqual(feed_url, 'fake url')

    def test_cycle(self):
        """Unit test for the cycle method
        When Cycle is run:
        *
        """
        # Arrange
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


if __name__ == '__main__':
    unittest.main()
