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
        with patch('H5_News_Tracker.gui.ticker_window.tk.Label', new_callable=PropertyMock) as mock_font_color:
            root = mock_font_color()
            app = TickerWindow(master=root)
            color = 'red'
            app.font_red()
            mock_font_color.assert_has_calls(mock_font_color.configure(background=color))

    def test_font_8(self):
        """Testing the menu font size"""
        with patch('H5_News_Tracker.gui.ticker_window.tk.Label', new_callable=PropertyMock) as mock_size:
            root = mock_size.Tk()
            app = TickerWindow(master=root)
            size = 8
            app.font_8()
            mock_size.assert_has_calls(mock_size.configure(size=size))

    def test_bg_white(self):
        """Testing the menu background color"""
        with patch('H5_News_Tracker.gui.ticker_window.tk.Label', new_callable=PropertyMock) as mock_bg_color:
            root = mock_bg_color.Tk()
            app = TickerWindow(master=root)
            color = 'white'
            app.bg_white()
            mock_bg_color.assert_has_calls(mock_bg_color.configure(background=color))


if __name__ == '__main__':
    unittest.main()
