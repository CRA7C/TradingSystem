import unittest
from unittest.mock import Mock, patch
from nemo_driver import NemoDriver


class TestNemoDriver(unittest.TestCase):

    def setUp(self):
        self.driver = NemoDriver()

    @patch('nemo_driver.NemoAPI')
    def test_login(self, MockNemoAPI):
        mock_api = MockNemoAPI()
        self.driver.api = mock_api
        self.driver.login('test_id', 'test_pass')
        mock_api.certification.assert_called_once_with('test_id', 'test_pass')

    @patch('nemo_driver.NemoAPI')
    def test_buy(self, MockNemoAPI):
        mock_api = MockNemoAPI()
        self.driver.api = mock_api
        self.driver.buy('0001', 100, 10)
        mock_api.purchasing_stock.assert_called_once_with('0001', 100, 10)

    @patch('nemo_driver.NemoAPI')
    def test_sell(self, MockNemoAPI):
        mock_api = MockNemoAPI()
        self.driver.api = mock_api
        self.driver.sell('0001', 100, 10)
        mock_api.selling_stock.assert_called_once_with('0001', 100, 10)

    @patch('nemo_driver.NemoAPI')
    def test_get_price(self, MockNemoAPI):
        mock_api = MockNemoAPI()
        self.driver.api = mock_api
        self.driver.get_price('0001')
        mock_api.get_market_price.assert_called_once_with('0001', 'current')


if __name__ == '__main__':
    unittest.main()
