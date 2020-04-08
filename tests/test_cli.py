"""
Tests for Command Line Interface
"""
import unittest
from H5_News_Tracker.controller import cli



def parse_args(self):
    pass


class TestCli(unittest.TestCase):

    def test_parse_args(self):
        parser = parse_args(['--url'])
        self.assertTrue(parser.url)


if __name__ == '__main__':
    unittest.main()
