"""Tests for main.py"""
import unittest
import threading
import time
from mock import Mock
from H5_News_Tracker.controller import main


class TestMain(unittest.TestCase):

    def test_cycle(self):
        """Unit test for the cycle method
        When Cycle is run:
        *
        """
        # Arrange
        mock_ticker = Mock()
        test_lib = [["headline_0", "https://test_0.com"], ["headline_1", "https://test_1.com"], ["headline_2", "https://test_2.com"]]
        test_thread = threading.Thread(target=main.cycle, args=[mock_ticker, test_lib], name="Test-Cycle-Thread")
        print(test_lib)

        try:
            # Act
            test_thread.start()
            print(mock_ticker.mock_calls)

            # Assert
            time.sleep(main.CYCLE_TIME/2)
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
