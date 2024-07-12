import unittest
from unittest.mock import Mock, patch
from kiwer_driver import KiwerDriver  # noqa
from nemo_driver import NemoDriver  # noqa
from auto_trading_system import AutoTradingSystem  # noqa


class TestAutoTradingSystem(unittest.TestCase):

    def setUp(self):
        self.system = AutoTradingSystem()

    def test_select_stock_broker_kiwer(self):
        self.system.select_stock_broker('kiwer')
        self.assertIsInstance(self.system.broker, KiwerDriver)

    def test_select_stock_broker_nemo(self):
        self.system.select_stock_broker('nemo')
        self.assertIsInstance(self.system.broker, NemoDriver)

    def test_login(self):
        self.system.broker = Mock()
        self.system.login('test_id', 'test_pass')
        self.system.broker.login.assert_called_once_with('test_id', 'test_pass')

    def test_buy(self):
        self.system.broker = Mock()
        self.system.buy('0001', 100, 10)
        self.system.broker.buy.assert_called_once_with('0001', 100, 10)

    def test_sell(self):
        self.system.broker = Mock()
        self.system.sell('0001', 100, 10)
        self.system.broker.sell.assert_called_once_with('0001', 100, 10)

    def test_get_price(self):
        self.system.broker = Mock()
        self.system.get_price('0001')
        self.system.broker.get_price.assert_called_once_with('0001')

    def test_buy_nice_timing(self):
        self.system.broker = Mock()
        self.system.get_price = Mock(side_effect=[90, 100, 110, 120, 130])
        self.system.buy = Mock()

        self.system.buy_nice_timing('0001', 1000)
        self.system.get_price.assert_called_with('0001')
        self.system.buy.assert_called_once_with('0001', 100, 10)

    def test_sell_nice_timing(self):
        self.system.broker = Mock()
        self.system.get_price = Mock(side_effect=[110, 100, 90, 80, 70])
        self.system.sell = Mock()

        self.system.sell_nice_timing('0001', 10)
        self.system.get_price.assert_called_with('0001')
        self.system.sell.assert_called_once_with('0001', 100, 10)

    # 종목 코드 규칙
    def test_validate_stock_code(self):
        self.system.validate_stock_code('005930')  # Valid code
        self.system.validate_stock_code('A005930')  # Valid code
        self.system.validate_stock_code('000660')  # Valid code
        self.system.validate_stock_code('A000660')  # Valid code
        with self.assertRaises(ValueError):
            self.system.validate_stock_code('00001')  # Invalid code
        with self.assertRaises(ValueError):
            self.system.validate_stock_code('Z00001')  # Invalid code

    # 자산 기능 추가
    def test_get_asset_status(self):
        status = self.system.get_asset_status()
        self.assertEqual(status['amount'], 1000000)
        status = self.system.get_asset_status()

        # 삼성전자 주식 구매
        self.system.buy('005930', 84000, 5)  # 삼성전자 주식
        status = self.system.get_asset_status()
        self.assertEqual(status['amount'], 580000)

        # 하이닉스 주식 구매
        self.system.buy('000660', 231500, 2)  # 하이닉스 주식
        status = self.system.get_asset_status()
        self.assertEqual(status['amount'], 117000)
        self.assertDictEqual(status['portfolio'], {
            '005930': 5,
            '000660': 2
        })



if __name__ == '__main__':
    unittest.main()
