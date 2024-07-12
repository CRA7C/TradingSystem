import unittest
from unittest.mock import Mock, patch
from kiwer_driver import KiwerDriver  # noqa
from Nemo_driver import NemoDriver  # noqa
from auto_trading_system import AutoTradingSystem  # noqa


class TestAutoTradingSystem(unittest.TestCase):

    def setUp(self):
        self.system = AutoTradingSystem()

    @patch('kiwer_driver.KiwerDriver')
    def test_select_stock_brocker_kiwer(self, MockKiwerDriver):
        self.system.select_stock_brocker('kiwer')
        self.assertIsInstance(self.system.brocker, MockKiwerDriver)

    @patch('Nemo_driver.NemoDriver')
    def test_select_stock_brocker_nemo(self, MockNemoDriver):
        self.system.select_stock_brocker('nemo')
        print(type(MockNemoDriver))
        self.assertIsInstance(self.system.brocker, MockNemoDriver)

    def test_login(self):
        self.system.brocker = Mock()
        self.system.login('test_id', 'test_pass')
        self.system.brocker.login.assert_called_once_with('test_id', 'test_pass')

    def test_buy(self):
        self.system.brocker = Mock()
        self.system.buy('0001', 100, 10)
        self.system.brocker.buy.assert_called_once_with('0001', 100, 10)

    def test_sell(self):
        self.system.brocker = Mock()
        self.system.sell('0001', 100, 10)
        self.system.brocker.sell.assert_called_once_with('0001', 100, 10)

    def test_get_price(self):
        self.system.brocker = Mock()
        self.system.get_price('0001')
        self.system.brocker.get_price.assert_called_once_with('0001')


if __name__ == '__main__':
    unittest.main()
