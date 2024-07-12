from mock_api import MockApi
from stock_brocker_driver_interface import StockerBrockerDriverInterface


class MockDriver(StockerBrockerDriverInterface):
    def __init__(self):
        self.api = MockApi()

    def login(self, id, passwd):
        self.api.login(id, passwd)

    def buy(self, code, quantity, price):
        self.api.buy(code, quantity, price)

    def sell(self, code, quantity, price):
        self.api.sell(code, quantity, price)

    def get_price(self, code):
        self.api.current_price(code)
