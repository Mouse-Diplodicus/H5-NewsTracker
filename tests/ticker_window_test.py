import tkinter
from unittest.mock import PropertyMock
from unittest.mock import patch
import unittest
from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestTickerWindow(unittest.TestCase):
    def test_menu_bar(self):
        """Testing the TickerWindow function menu_bar()"""
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.menu_bar') as mocked_menu_bar:
            root = tkinter.Tk()
            app = TickerWindow(master=root)

            app.menu_bar()
            mocked_menu_bar.assert_any_call()



if __name__ == '__main__':
    unittest.main()
