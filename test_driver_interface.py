import unittest
from stock_brocker_driver_interface import StockerBrockerDriverInterface


class TestStockerBrockerDriverInterface(unittest.TestCase):

    def test_interface_methods(self):
        with self.assertRaises(TypeError):
            driver = StockerBrockerDriverInterface()  # 추상 메서드이기에 에러 발생
            driver.login('id', 'pass')
            driver.buy('0001', 100, 10)
            driver.sell('0001', 100, 10)
            driver.get_price('0001')


if __name__ == '__main__':
    unittest.main()
