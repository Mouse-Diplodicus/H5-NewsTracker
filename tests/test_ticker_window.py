import unittest
from unittest.mock import patch
from unittest.mock import PropertyMock
import tkinter
from tkinter import ttk
from H5_News_Tracker.gui import ticker_window
from H5_News_Tracker.controller import main


class TestTickerWindow(unittest.TestCase):

    def test_start(self):
        with patch('tkinter.Tk') as mocked_ticker:
            mock_root = mocked_ticker()
            app = ticker_window.TickerWindow(master=mock_root)
            app.start()
            mock_root.assert_has_calls(mock_root.mainloop())

    def test_set_style(self):
        with patch('tkinter.ttk.Style', new_callable=PropertyMock) as mock_style:
            with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
                with patch('tkinter.ttk.Button', new_callable=PropertyMock) as mock_button:
                    root = tkinter.Tk()
                    app = ticker_window.TickerWindow(master=root)
                    test_label = mock_label(root)
                    test_button = mock_button(root)
                    app.set_style()
                    mock_style.assert_has_calls(mock_style.configure("default.TLabel", foreground="#000000", background="#ffffff"))
                    mock_style.assert_has_calls(mock_style.configure("WB.TLabel", foreground="#ffffff", background="#000000", relief="GROOVE"))
                    mock_style.assert_has_calls(mock_style.configure("Exit.TLabel", foreground="#000000", background="#931113", relief="RAISED"))
                    test_label.assert_has_calls(test_label.configure(style="WB.TLabel"))
                    test_button.assert_has_calls(test_button.configure(style="Exit.TLabel"))

    def test_build(self):
        with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
            with patch('tkinter.ttk.Button', new_callable=PropertyMock) as mock_button:
                root = tkinter.Tk()
                app = ticker_window.TickerWindow(master=root)
                test_label = mock_label(root)
                test_button = mock_button(root)
                app.build()
                test_label.assert_has_calls(test_label.grid(row=0, column=0))
                test_button.assert_has_calls(test_button.grid(row=0, column=1))



    def test_update(self):
        with patch('H5_News_Tracker.gui.ticker_window.tkinter') as mocked_tkinter:
            headline = 'test headline'
            url = 'testurl.com'
            # mocked_root = mocked_tkinter.Tk()
            # mocked_label = ttk.Label(mocked_root)
            # mocked_label.configure.assert_called_with(text=headline)
            # mocked_label.configure.assert_called_with("<Button-1>", lambda e: webbrowser.open_new(url))
