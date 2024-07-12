class MockApi:
    def login(self, id, password):
        pass

    def buy(self, stock_code, count, price):
        pass

    def sell(self, stock_code, count, price):
        pass

    def current_price(self, stock_code) -> int:
        pass
