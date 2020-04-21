"""Tests for main.py"""
import threading
import time
import tkinter
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import main
from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.parser import feed_interface


class TestMain(unittest.TestCase):

    def test_build_news_ticker(self):
        """Testing the build_news_ticker function """
        with patch('H5_News_Tracker.parser.feed_interface.build_library') as mocked_build_library:
            with patch('H5_News_Tracker.parser.feed_interface.parse') as mocked_parser:
                with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
                    with patch('H5_News_Tracker.controller.main.threading.Thread') as mocked_thread:
                        with patch('H5_News_Tracker.controller.main.cycle') as mocked_cycle:
                            main.build_news_ticker('https://test.com')
                            root = tkinter.Tk()
                            test_library = feed_interface.build_library(feed_interface.parse('https://test.com'))
                            # Assertions
                            mocked_build_library.assert_called_with(mocked_parser('https://test.com'))
                            mocked_ticker_window.assert_called_with(master=root)
                            mocked_thread.assert_called_with(mocked_thread(target=mocked_cycle, args=[
                                mocked_ticker_window, test_library], name="News-Cycling-Thread", daemon=True))
                            mocked_ticker_window.assert_has_calls(TickerWindow.start())

    def test_cycle(self):
        """
        Unit test for the cycle method
        When Cycle is run: it should call the update() function on the ticker it is passed after the Cycle_time
        has passed
        """
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mock_ticker:
            # with patch('H5_News_Tracker.parser.feed_interface.ThreadSafeList') as mocked_list:
            test_list = feed_interface.ThreadSafeList
            root = tkinter.Tk()
            mock_ticker(master=root)
            test_list.append(["headline_0", "https://test_0.com"])
            test_list.append(["headline_1", "https://test_1.com"])
            test_list.append(["headline_2", "https://test_2.com"])
            test_thread = threading.Thread(target=main.cycle, args=[mock_ticker, test_list], name="Test-Cycle-Thread")

            print(test_list.count)

            try:
                    # Act
                test_thread.start()

                    # Assert
                time.sleep(main.CYCLE_TIME / 2)
                mock_ticker.update.assert_called_with(["headline_0", "https://test_0.com"])
                time.sleep(main.CYCLE_TIME)
                mock_ticker.update.assert_called_with(test_list[1][0], test_list[1][1])
                time.sleep(main.CYCLE_TIME)
                mock_ticker.update.assert_called_with(test_list[2][0], test_list[2][1])
            except AssertionError as err:
                raise err
            except BaseException as err:
                msg = "'cycle' command should not throw errors: " + repr(err)
                raise AssertionError(msg)


if __name__ == '__main__':
    unittest.main()
