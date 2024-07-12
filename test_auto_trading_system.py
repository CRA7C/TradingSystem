import unittest
from unittest.mock import Mock, patch
from kiwer_driver import KiwerDriver  # noqa
from nemo_driver import NemoDriver  # noqa
from auto_trading_system import AutoTradingSystem  # noqa


class TestAutoTradingSystem(unittest.TestCase):

    def setUp(self):
        self.system = AutoTradingSystem()

    def test_select_stock_brocker_kiwer(self):
        self.system.select_stock_brocker('kiwer')
        self.assertIsInstance(self.system.brocker, KiwerDriver)

    def test_select_stock_brocker_nemo(self):
        self.system.select_stock_brocker('nemo')
        self.assertIsInstance(self.system.brocker, NemoDriver)

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

    def test_buy_nice_timing(self):
        self.system.brocker = Mock()
        self.system.get_price = Mock(side_effect=[90, 100, 110, 120, 130])
        self.system.buy = Mock()

        self.system.buy_nice_timing('0001', 1000)
        self.system.get_price.assert_called_with('0001')
        self.system.buy.assert_called_once_with('0001', 100, 10)

    def test_sell_nice_timing(self):
        self.system.brocker = Mock()
        self.system.get_price = Mock(side_effect=[110, 100, 90, 80, 70])
        self.system.sell = Mock()

        self.system.sell_nice_timing('0001', 10)
        self.system.get_price.assert_called_once_with('0001')
        self.system.sell.assert_called_once_with('0001', 100, 10)


if __name__ == '__main__':
    unittest.main()
