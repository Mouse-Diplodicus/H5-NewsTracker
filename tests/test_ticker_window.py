import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from tkinter import ttk
import webbrowser
from H5_News_Tracker.gui import ticker_window
from H5_News_Tracker.controller import main


class TestTickerWindow(unittest.TestCase):

    def test_start(self):
        with patch('H5_News_Tracker.gui.ticker_window.tkinter') as mocked_tkinter:
            self.mocked_root = mocked_tkinter.Tk()
            # main.build_rss_ticker()
            # self.mocked_root.mainloop.assert_any_call()

    def test_set_style(self):
        pass

    def test_build(self):
        with patch('H5_News_Tracker.gui.ticker_window.tkinter') as mocked_tkinter:
            self.mocked_root = mocked_tkinter.Tk()
            self.mocked_label = ttk.Label(self.mocked_root)
            # main.build_rss_ticker()
            # self.mocked_label.grid.assert_called_with(row=0, column=0)

    def test_update(self):
        with patch('H5_News_Tracker.gui.ticker_window.tkinter') as mocked_tkinter:
            headline = 'test headline'
            url = 'testurl.com'
            mocked_root = mocked_tkinter.Tk()
            mocked_label = ttk.Label(mocked_root)
            # mocked_label.configure.assert_called_with(text=headline)
            # mocked_label.configure.assert_called_with("<Button-1>", lambda e: webbrowser.open_new(url))
