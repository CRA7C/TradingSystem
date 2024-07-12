import unittest
from unittest.mock import Mock, patch
from kiwer_driver import KiwerDriver


class TestKiwerDriver(unittest.TestCase):

    def setUp(self):
        self.driver = KiwerDriver()
        self.mock_api = Mock()
        self.driver.api = self.mock_api

    def test_login(self):
        self.driver.login('test_id', 'test_pass')
        self.mock_api.login.assert_called_once_with('test_id', 'test_pass')

    def test_buy(self):
        self.driver.buy('0001', 100, 10)
        self.mock_api.buy.assert_called_once_with('0001', 100, 10)

    def test_sell(self):
        self.driver.sell('0001', 100, 10)
        self.mock_api.sell.assert_called_once_with('0001', 100, 10)

    def test_get_price(self):
        self.driver.get_price('0001')
        self.mock_api.current_price.assert_called_once_with('0001')


if __name__ == '__main__':
    unittest.main()
