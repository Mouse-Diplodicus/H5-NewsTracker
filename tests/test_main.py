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
            with patch('H5_News_Tracker.parser.feed_interface.ThreadSafeList') as mocked_list:
                with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.update_headline') as mocked_update:
                    # mocked_list = [["headline_0", "https://test_0.com"], ["headline_1", "https://test_1.com"], ["headline_2", "https://test_2.com"]]
                    mocked_list.append(["headline_0", "https://test_0.com"])
                    mocked_list.append(["headline_1", "https://test_1.com"])
                    mocked_list.append(["headline_2", "https://test_2.com"])
                    root = tkinter.Tk()
                    test_ticker = mock_ticker(master=root)
                    test_thread = threading.Thread(target=main.cycle, args=[test_ticker, mocked_list], name="Test-Cycle-Thread")


                    try:
                        # Act
                        test_thread.start()

                        test_item = mocked_list.iterate(0)
                        test_item1 = mocked_list.iterate(1)
                        test_item2 = mocked_list.iterate(2)

                        # Assert
                        time.sleep(main.CYCLE_TIME / 2)
                        test_ticker.update_headline.assert_called_with(test_item[0], test_item[1])
                        time.sleep(main.CYCLE_TIME)
                        test_ticker.update_headline.assert_called_with(test_item1[0], test_item1[1])
                        time.sleep(main.CYCLE_TIME)
                        test_ticker.update_headline.assert_called_with(test_item2[0], test_item2[1])
                    except AssertionError as err:
                        raise err
                    except BaseException as err:
                        msg = "'cycle' command should not throw errors: " + repr(err)
                        raise AssertionError(msg)


if __name__ == '__main__':
    unittest.main()
