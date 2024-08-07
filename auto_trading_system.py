import re

from kiwer_driver import KiwerDriver
from mock_driver import MockDriver
from nemo_driver import NemoDriver


class AutoTradingSystem:
    def __init__(self):
        self.asset = None
        self.broker = None
        self.stock_broker_dict = {
            'kiwer': KiwerDriver,
            'nemo': NemoDriver,
            'mock': MockDriver,
        }

        self.validation_pattern = re.compile('^[ABCK]?[0-9]{6}$')
        self.status = {
            "amount": 1000000,
            "portfolio": dict()
        }

    def select_stock_broker(self, param):
        if param not in self.stock_broker_dict.keys():
            raise ValueError(f"{param} stock broker does not exist.")
        self.broker = self.stock_broker_dict[param]()

    def login(self, id, password):
        self.broker.login(id, password)

    def buy(self, code, price, quantity):
        if self.status["amount"] < price * quantity:
            raise ValueError(f"cash is not enough {self.status['amount']} < {price} * {quantity}")
        self.broker.buy(code, price, quantity)
        check_stock = code in self.status["portfolio"]
        if check_stock:
            self.status["portfolio"][code] += quantity
        else:
            self.status["portfolio"][code] = quantity
        self.status["amount"] -= price * quantity

    def sell(self, code, price, quantity):
        if code not in self.status['portfolio']:
            raise ValueError(f'해당 종목을 보유하고 있지 않습니다. code: {code}')
        if quantity > self.status['portfolio'][code]:
            raise ValueError(f"보유한 수량 안에서 판매 가능합니다. code: {code}, quantity: {quantity}")
        self.broker.sell(code, price, quantity)

    def get_price(self, code) -> int:
        return self.broker.get_price(code)

    def buy_nice_timing(self, code, money):
        prev_price = self.get_price(code)
        current_price = self.get_price(code)
        if prev_price < current_price:
            self.buy(code, current_price, money // current_price)

    def sell_nice_timing(self, code, quantity):
        prev_price = self.get_price(code)
        for i in range(5):
            curr_price = self.get_price(code)
            if curr_price < prev_price:
                self.sell(code, curr_price, quantity)
                break
            prev_price = curr_price

    def validate_stock_code(self, code):
        if self.validation_pattern.search(code) is None:
            raise ValueError

    def get_asset_status(self) -> dict:
        return self.status
