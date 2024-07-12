from nemo_api import NemoAPI
from stock_brocker_driver_interface import StockerBrokerDriverInterface


class NemoDriver(StockerBrokerDriverInterface):
    def __init__(self):
        self.api = NemoAPI()

    def login(self, id, passwd):
        self.api.cerification(id, passwd)

    def buy(self, code, quantity, price):
        self.api.purchasing_stock(code, price, quantity)

    def sell(self, code, quantity, price):
        self.api.selling_stock(code, price, quantity)

    def get_price(self, code):
        self.api.get_market_price(code, 0)
