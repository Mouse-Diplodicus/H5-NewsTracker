"""Tests for main.py"""
import threading
import time
import tkinter
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
                        main.build_rss_ticker()
                        root = tkinter.Tk()
                        # Assertions
                        main.build_news_ticker('https://news.google.com/news/rss')
                        mocked_build_library.assert_called_with(mocked_parser('https://news.google.com/news/rss'))
                        mocked_ticker_window.assert_called_with(master=root)
                        #mocked_thread.assert_called_with(mocked_thread(target=cycle, args=[mocked_ticker_window, mocked_pull_feed], name="News-Cycling-Thread", daemon=True))
                        mocked_ticker_window.assert_has_calls(TickerWindow.start())

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


if __name__ == '__main__':
    unittest.main()
