"""tests.test_ticker_window"""
import tkinter
import unittest
import webbrowser
import threading
from tkinter import font
from unittest.mock import PropertyMock
from unittest.mock import patch

from H5_News_Tracker.gui.ticker_window import TickerWindow
from H5_News_Tracker.controller import utilities


class TestTickerWindow(unittest.TestCase):
    """Testing class for gui.ticker_window"""

    @classmethod
    def setUp(cls):
        cls.root = tkinter.Tk()
        cls.test_config = utilities.load_config_file()['ticker_window']
        cls.test_window = TickerWindow(master=cls.root, config=cls.test_config)

    @classmethod
    def tearDown(cls):
        cls.test_window.destroy()

    def test_init(self):
        """Unit test for H5_News_tracker.gui.ticker_window.TickerWindow.__init__"""
        expected_padding = ('0', '-1', '0', '-1')
        expected_dict = {'!menu': '', '!menu2': '', '!menu3': ''}
        self.assertTrue(self.test_window.winfo_toplevel().title, 'H5-NewsTracker')
        self.assertEqual(self.test_window.font['size'], self.test_config['font_size'])
        self.assertEqual(self.test_window.font.name, 'TkDefaultFont')
        self.assertEqual(self.test_window.label_ticker['style'], 'default.TLabel')
        print(self.test_window.label_ticker['padding'])
        self.assertEqual(expected_padding, self.test_window.label_ticker.cget('padding'))
        self.assertEqual(expected_dict.keys(), self.test_window.menubar.children.keys())

    def test_change_background_color(self):
        pass

    def test_change_text_color(self):
        pass

    def test_change_font_size(self):
        pass

    def test_start(self):
        """Unit test for H5_News_tracker.gui.ticker_window.TickerWindow.start()"""
        print('testing start')
        kill_thread = threading.Thread(target=self.test_window.close, args=[3], name="Test-Kill-Thread", daemon=True)
        kill_thread.start()
        with patch('tkinter.Tk') as mocked_tk:
            mock_master = mocked_tk()
            self.test_window.start()
            mock_master.assert_has_calls(mock_master.mainloop())

    def test_update_headline(self):
        """Unit test for H5_News_tracker.gui.ticker_window.TickerWindow.update_headline()"""
        with patch('tkinter.ttk.Label', new_callable=PropertyMock) as mock_label:
            headline = 'test headline'
            headline1 = ""
            headline2 = None
            url = 'test_url.com'
            url1 = ""
            url2 = None
            test_label = mock_label(self.root)

            self.test_window.update_headline(headline, url)
            test_label.assert_has_calls(test_label.configure('test headline'),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new('test_url.com')))
            self.test_window.update_headline(headline1, url1)
            test_label.assert_has_calls(test_label.configure(""),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new("")))
            self.test_window.update_headline(headline2, url2)
            test_label.assert_has_calls(test_label.configure(None),
                                        test_label.bind("<Button-1>", lambda e: webbrowser.open_new(None)))

    def test_size_headline(self):
        """Unit test for H5_News_tracker.gui.ticker_window.TickerWindow.size_headline"""
        test_input_1 = "Hey Guys How's it going"
        test_input_2 = "I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble?" \
                       " Also I am a very redundant person"
        test_input_3 = "If you like piña coladas and getting caught in the rain. If you're not into yoga, get out " \
                       "now! I don't even like this song"
        test_font = self.test_window.font
        max_label_pixel_width = font.Font.measure(test_font, "n") * TickerWindow.max_label_width
        self.assertEqual("Hey Guys How's it going", self.test_window.size_headline(test_input_1))
        self.assertEqual("I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble?"
                         " Also I am a v...", self.test_window.size_headline(test_input_2))
        self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font,
                                                                         self.test_window.size_headline(test_input_2)))
        self.assertEqual("If you like piña coladas and getting caught in the rain. If you're not into yoga, get out no"
                         "w! I don't even ...", self.test_window.size_headline(test_input_3))
        self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font,
                                                                         self.test_window.size_headline(test_input_3)))

    def test_close(self):
        """Unit test for H5_News_tracker.gui.ticker_window.TickerWindow.test_close"""
        pass
