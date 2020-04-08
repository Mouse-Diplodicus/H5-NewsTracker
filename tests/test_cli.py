"""
Tests for Command Line Interface
"""
import unittest
from unittest.mock import MagicMock
from H5_News_Tracker.controller import cli


class TestCli(unittest.TestCase):

    def test_parse_args_default(self):
        parser = cli.parse_args([])
        self.assertFalse(parser.url)

    def test_parse_args(self):
        parser = cli.parse_args(['--url'])
        self.assertTrue(self, parser.url)
        parser = cli.parse_args(['--file'])
        self.assertTrue(self, parser.file)
        parser = cli.parse_args(['--config'])
        self.assertTrue(self, parser.config)


if __name__ == '__main__':
    unittest.main()
