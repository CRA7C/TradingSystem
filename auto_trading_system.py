from kiwer_driver import KiwerDriver
from nemo_driver import NemoDriver


class AutoTradingSystem:
    def __init__(self):
        self.prev_price = {}
        self.NemoDriver = None
        self.KiwerDriver = None
        self.brocker = None

    def select_stock_brocker(self, param):
        if param not in ['kiwer', 'nemo']:
            raise ValueError(f"{param} stock brocker does not exist.")

        if param == 'kiwer':
            self.brocker = KiwerDriver()
        if param == 'nemo':
            self.brocker = NemoDriver()

    def login(self, id, password):
        self.brocker.login(id, password)

    def buy(self, code, price, quantity):
        self.brocker.buy(code, price, quantity)

    def sell(self, code, price, quantity):
        self.brocker.sell(code, price, quantity)

    def get_price(self, code) -> int:
        return self.brocker.get_price(code)

    def buy_nice_timing(self, code, money):
        self.prev_price[code] = self.get_price(code)
        current_price = self.get_price(code)
        if self.prev_price[code] < current_price:
            self.buy(code, current_price, money // current_price)
            
    def sell_nice_timing(self, code, quantity):
        prev_price = self.get_price(code)
        for i in range(5):
            curr_price = self.get_price(code)
            if curr_price < prev_price:
                self.sell(code, curr_price, quantity)
                break
            prev_price = curr_price
            