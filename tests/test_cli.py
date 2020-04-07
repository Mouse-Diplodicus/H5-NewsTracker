""" Tests for Command Line Interface """
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import cli


class TestCli(unittest.TestCase):

    def test_parse_args(self):
        #cli = MagicMock()
        #parsed = cli.parse_args(['--url', 'test'])
        #self.assertEqual(parsed.parse_args, 'test')
        pass

if __name__ == '__main__':
    unittest.main()
