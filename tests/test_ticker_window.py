import unittest
from tkinter import font
from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestTickerWindow(unittest.TestCase):

    def test_start(self):
        pass

    def test_set_style(self):
        pass

    def test_build(self):
        pass

    def test_update(self):
        pass

    def test_size_headline(self):
        test_input_1 = "Hey Guys How's it going"
        test_input_2 = "I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble? Also I am a very redundant person"
        test_input_3 = "If you like piña coladas and getting caught in the rain. If you're not into yoga, get out now! I don't even like this song"
        tw = TickerWindow()
        test_font = tw.default_font
        max_label_pixel_width = font.Font.measure(test_font, "n") * TickerWindow.max_label_width
        self.assertEqual("Hey Guys How's it going", tw.size_headline(test_input_1))
        self.assertEqual("I really like to ramble and I repeat myself a lot. Have I told you how much I like to ramble? Also I am a v...", tw.size_headline(test_input_2))
        self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font, tw.size_headline(test_input_2)))
        self.assertEqual("If you like piña coladas and getting caught in the rain. If you're not into yoga, get out now! I don't even ...", tw.size_headline(test_input_3))
        self.assertGreaterEqual(max_label_pixel_width, font.Font.measure(test_font, tw.size_headline(test_input_3)))