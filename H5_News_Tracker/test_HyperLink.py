import unittest
import tkinter as tk
import HyperLink
import hello


class TestHyperLink(unittest.TestCase):

    def setUp(self):
        root = tk.Tk()
        link1 = tk.Label(root, text="Reddit Hyperlink", fg="black", cursor="hand2")
        link1.pack()
        root.mainloop()

    def test_mock_reddit_link(self):
        pass
    

    def test_open_RSS_Ticker(self):



if __name__ == '__main__':
    unittest.main()