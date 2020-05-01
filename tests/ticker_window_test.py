import tkinter
from unittest.mock import PropertyMock
from unittest.mock import patch
import unittest
from H5_News_Tracker.gui.ticker_window import TickerWindow


class TestTickerWindow(unittest.TestCase):
    def test_menu_bar(self):
        with patch('tkinter.ttk.Menu', new_callable=PropertyMock) as mocked_menu_bar:
            root = tkinter.Tk()
            app = TickerWindow(master=root)
            test_menu_bar = mocked_menu_bar(root)

            app.menu_bar()
            test_menu_bar.assert_any_call()



if __name__ == '__main__':
    unittest.main()
