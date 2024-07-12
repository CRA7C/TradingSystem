import unittest
from unittest.mock import Mock, patch
from nemo_api import NemoAPI
from nemo_driver import NemoDriver


class TestNemoDriver(unittest.TestCase):

    def setUp(self):
        self.driver = NemoDriver()
        self.mock_api = Mock(spec=NemoAPI)
        self.driver.api = self.mock_api

    def test_login(self):
        self.driver.login('test_id', 'test_pass')
        self.mock_api.certification.assert_called_once_with('test_id', 'test_pass')

    def test_buy(self):
        self.driver.buy('0001', 100, 10)
        self.mock_api.purchasing_stock.assert_called_once_with('0001', 100, 10)

    def test_sell(self):
        self.driver.sell('0001', 100, 10)
        self.mock_api.selling_stock.assert_called_once_with('0001', 100, 10)

    def test_get_price(self):
        self.driver.get_price('0001')
        self.mock_api.get_market_price.assert_called_once_with('0001', 'current')


if __name__ == '__main__':
    unittest.main()
