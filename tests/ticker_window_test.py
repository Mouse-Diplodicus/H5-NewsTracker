import tkinter
from unittest.mock import PropertyMock
from unittest.mock import call, patch, MagicMock
import unittest
from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestTickerWindow(unittest.TestCase):
    def test_menu_bar(self):
        """Testing the TickerWindow function menu_bar()"""
        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.menu_bar') as mock_menu_bar:
            root = tkinter.Tk()
            app = TickerWindow(master=root)
            app.menu_bar()
            mock_menu_bar.assert_any_call()

    def test_font_red(self):
        """Testing the menu font color"""
        color = "red"
        with patch('tkinter.Tk') as mock_ticker:
            mock_root = mock_ticker()
            tw = TickerWindow(master=mock_root)
            self.assertEqual("red", tw.font_red(color))


if __name__ == '__main__':
    unittest.main()
