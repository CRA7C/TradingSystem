import unittest
from unittest.mock import Mock, patch
from kiwer_driver import KiwerDriver


class TestKiwerDriver(unittest.TestCase):

    def setUp(self):
        self.driver = KiwerDriver()

    @patch('kiwer_driver.KiwerAPI')
    def test_login(self, MockKiwerAPI):
        mock_api = MockKiwerAPI()
        self.driver.api = mock_api
        self.driver.login('test_id', 'test_pass')
        mock_api.login.assert_called_once_with('test_id', 'test_pass')

    @patch('kiwer_driver.KiwerAPI')
    def test_buy(self, MockKiwerAPI):
        mock_api = MockKiwerAPI()
        self.driver.api = mock_api
        self.driver.buy('0001', 100, 10)
        mock_api.buy.assert_called_once_with('0001', 100, 10)

    @patch('kiwer_driver.KiwerAPI')
    def test_sell(self, MockKiwerAPI):
        mock_api = MockKiwerAPI()
        self.driver.api = mock_api
        self.driver.sell('0001', 100, 10)
        mock_api.sell.assert_called_once_with('0001', 100, 10)

    @patch('kiwer_driver.KiwerAPI')
    def test_get_price(self, MockKiwerAPI):
        mock_api = MockKiwerAPI()
        self.driver.api = mock_api
        self.driver.get_price('0001')
        mock_api.current_price.assert_called_once_with('0001')


if __name__ == '__main__':
    unittest.main()
