"""Tests for main.py"""
import unittest
import threading
import time
from unittest.mock import Mock
from unittest.mock import MagicMock
from unittest.mock import patch
from H5_News_Tracker.controller import main


class TestMain(unittest.TestCase):
    mocked_pull_feed = MagicMock()
    mocked_build_library = MagicMock()

    # @patch('main.build_library()', mocked_build_library)
    # @patch('main.pull_feed()', mocked_pull_feed)
    def test_build_rss_ticker(self):
        with patch('H5_News_Tracker.controller.main.build_rss_ticker') as mocked_ticker:
            mocked_ticker.return_value = 'ticker'
            self.assertIsNotNone(main.build_rss_ticker())

    def test_cycle(self):
        """Unit test for the cycle method
        When Cycle is run:
        *
        """
        # Arrange
        mock_ticker = Mock()
        test_lib = [["headline_0", "https://test_0.com"], ["headline_1", "https://test_1.com"],
                    ["headline_2", "https://test_2.com"]]
        test_thread = threading.Thread(target=main.cycle, args=[mock_ticker, test_lib], name="Test-Cycle-Thread")

        try:
            # Act
            test_thread.start()

            # Assert
            time.sleep(main.CYCLE_TIME / 2)
            mock_ticker.update.assert_called_with(test_lib[0][0], test_lib[0][1])
            time.sleep(main.CYCLE_TIME)
            mock_ticker.update.assert_called_with(test_lib[1][0], test_lib[1][1])
            time.sleep(main.CYCLE_TIME)
            mock_ticker.update.assert_called_with(test_lib[2][0], test_lib[2][1])
        except AssertionError as err:
            raise err
        except BaseException as err:
            msg = "'cycle' command should not throw errors: " + repr(err)
            raise AssertionError(msg)


if __name__ == '__main__':
    unittest.main()
