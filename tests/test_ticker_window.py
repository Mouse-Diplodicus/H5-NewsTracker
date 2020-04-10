import unittest
from unittest.mock import patch
from unittest.mock import PropertyMock
import tkinter
from H5_News_Tracker.gui import ticker_window
import webbrowser


class TestTickerWindow(unittest.TestCase):

    def test_start(self):
        """Testing the TickerWindow Function start()"""
        with patch('tkinter.Tk') as mocked_ticker:
            mock_root = mocked_ticker()
            app = ticker_window.TickerWindow(master=mock_root)
            app.start()
            mock_root.assert_has_calls(mock_root.mainloop())

    def test_set_style(self):
        """Testing the TickerWindow Function set_style()"""
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
        """Testing the TickerWindow Function build()"""
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
        """Testing the TickerWindow Function update()"""
        with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
            headline = 'test headline'
            headline1 = ""
            headline2 = None
            url = 'testurl.com'
            url1 = ""
            url2 = None
            root = tkinter.Tk()
            app = ticker_window.TickerWindow(master=root)
            test_label = mock_label(root)
            app.update(headline, url)
            test_label.assert_has_calls(test_label.configure('test headline'),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new('testurl.com')))
            app.update(headline1, url1)
            test_label.assert_has_calls(test_label.configure(""),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new("")))
            app.update(headline2, url2)
            test_label.assert_has_calls(test_label.configure(None),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new(None)))