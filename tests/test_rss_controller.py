"""Tests for rss_controller.py"""
import threading
import time
import tkinter
import unittest
from unittest.mock import patch
from H5_News_Tracker.controller import rss_controller
from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.parser import feed_interface
from H5_News_Tracker.parser.feed_interface import ThreadSafeList


class TestMain(unittest.TestCase):

    def test_build_news_ticker(self):
        """
        Testing the build_news_ticker function
        """

        # Initializing
        test_urls = ['https://test.com']
        root = tkinter.Tk()

        with patch('H5_News_Tracker.parser.feed_interface.build_library') as mocked_build_library:
            with patch('H5_News_Tracker.parser.feed_interface.parse') as mocked_parser:
                # Action
                rss_controller.build_news_ticker(test_urls)
                # Assertions
                mocked_build_library.assert_called_with(mocked_parser('https://test.com'))
                # mocked_build_library.assert_called_with(mocked_parser(''))
                # mocked_build_library.assert_called_with(mocked_parser(None))

        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mocked_ticker_window:
            # Action
            rss_controller.build_news_ticker(test_urls)
            # Assertions
            mocked_ticker_window.assert_called_with(master=root)
            mocked_ticker_window.assert_called_with(mocked_ticker_window.start())
            pass

        with patch('H5_News_Tracker.controller.rss_controller.threading.Thread') as mocked_thread:
            with patch('H5_News_Tracker.controller.rss_controller.cycle') as mocked_cycle:
                pass
                #mocked_thread.assert_called_with(target=mocked_cycle, args=[TickerWindow(master=root),
                 #                                test_lib], name="News-Cycling-Thread", daemon=True)

    def test_cycle(self):
        """
        Unit test for the cycle method
        When Cycle is run: it should call the update() function on the ticker it is passed after the Cycle_time
        has passed
        """
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow') as mock_ticker:
            with patch('H5_News_Tracker.parser.feed_interface.ThreadSafeList') as mocked_list:
                with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.update_headline') as mocked_update:
                    mocked_list.append(["headline_0", "https://test_0.com"])
                    mocked_list.append(["headline_1", "https://test_1.com"])
                    mocked_list.append(["headline_2", "https://test_2.com"])
                    root = tkinter.Tk()
                    test_ticker = mock_ticker(master=root)
                    test_thread = threading.Thread(target=rss_controller.cycle, args=[test_ticker, mocked_list], name="Test-Cycle-Thread")


                    try:
                        #Assert
                        test_item = mocked_list.iterate(0)
                        test_item1 = mocked_list.iterate(1)
                        test_item2 = mocked_list.iterate(2)

                        # Act
                        test_thread.start()

                        # Assert
                        time.sleep(rss_controller.CYCLE_TIME / 10)
                        test_ticker.update_headline.assert_called_with(test_item[0], test_item[1])
                        time.sleep(rss_controller.CYCLE_TIME / 10)
                        test_ticker.update_headline.assert_called_with(test_item1[0], test_item1[1])
                        time.sleep(rss_controller.CYCLE_TIME / 10)
                        test_ticker.update_headline.assert_called_with(test_item2[0], test_item2[1])
                    except AssertionError as err:
                        raise err
                    except BaseException as err:
                        msg = "'cycle' command should not throw errors: " + repr(err)
                        raise AssertionError(msg)


if __name__ == '__main__':
    unittest.main()
