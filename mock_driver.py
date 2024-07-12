from stock_brocker_driver_interface import StockerBrokerDriverInterface


class MockApi:
    def login(self, id, password):
        pass

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        pass

    def current_price(self, stock_code) -> int:
        pass


class MockDriver(StockerBrokerDriverInterface):
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
