import tkinter
import unittest
import webbrowser
from tkinter import font
from unittest.mock import PropertyMock
from unittest.mock import patch

from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestTickerWindow(unittest.TestCase):

    def test_init(self):
        """Testing the TickerWindow __init__ function"""
        with patch('tkinter.Tk') as mocked_ticker:
            with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
                with patch('tkinter.ttk.Button', new_callable=PropertyMock) as mock_button:
                    with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.set_style') as mocked_set_style:
                        with patch('H5_News_Tracker.gui.ticker_window.TickerWindow.build') as mocked_build:
                            mock_root = mocked_ticker()
                            app = TickerWindow(master=mock_root)
                            test_label = mock_label(mock_root)
                            test_button = mock_button(mock_root)
                            app.__init__(mock_root)

                            test_label.assert_has_calls(test_label.configure(width=70, padding=[0, -1, 0, -1]))
                            test_button.assert_has_calls(test_button.configure(text="X", padding=[2, -1, 2, -1], command=mock_root.quit))
                            mock_root.assert_has_calls(mock_root.overrideredirect(1))
                            mocked_set_style.assert_any_call()
                            mocked_build.assert_any_call()

    def test_start(self):
        """Testing the TickerWindow Function start()"""
        with patch('tkinter.Tk') as mocked_ticker:
            mock_root = mocked_ticker()
            app = TickerWindow(master=mock_root)
            app.start()
            mock_root.assert_has_calls(mock_root.mainloop())

    def test_set_style(self):
        """Testing the TickerWindow Function set_style()"""
        with patch('tkinter.ttk.Style', new_callable=PropertyMock) as mock_style:
            with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
                with patch('tkinter.ttk.Button', new_callable=PropertyMock) as mock_button:
                    root = tkinter.Tk()
                    app = TickerWindow(master=root)
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
                app = TickerWindow(master=root)
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
            app = TickerWindow(master=root)
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

    def test_size_headline(self):
        """Testing the TickerWindow size_headline"""
        test_input_1 = "Hey Guys How's it going"
        test_input_2 = "I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble?" \
                       " Also I am a very redundant person"
        test_input_3 = "If you like piña coladas and getting caught in the rain. If you're not into yoga, get out " \
                       "now! I don't even like this song"
        with patch('tkinter.Tk') as mocked_ticker:
            mock_root = mocked_ticker()
            tw = TickerWindow(master=mock_root)
            test_font = tw.default_font
            max_label_pixel_width = font.Font.measure(test_font, "n") * TickerWindow.max_label_width
            self.assertEqual("Hey Guys How's it going", tw.size_headline(test_input_1))
            self.assertEqual("I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble?"
                             " Also I am a v...", tw.size_headline(test_input_2))
            self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font, tw.size_headline(test_input_2)))
            self.assertEqual("If you like piña coladas and getting caught in the rain. If you're not into yoga, get out no"
                             "w! I don't even ...", tw.size_headline(test_input_3))
            self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font, tw.size_headline(test_input_3)))

