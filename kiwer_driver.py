from kiwer_api import KiwerAPI
from stock_brocker_driver_interface import StockerBrockerDriverInterface


class KiwerDriver(StockerBrockerDriverInterface):
    def __init__(self):
        self.api = KiwerAPI()

    def set_api(self, api):
        self.api = api

    def login(self, user, pw):
        self.api.login(user, pw)

    def buy(self, code, quantity, price):
        self.api.buy(code, quantity, price)

    def sell(self, code, quantity, price):
        self.api.sell(code, quantity, price)

    def get_price(self, code):
        self.api.current_price(code)
