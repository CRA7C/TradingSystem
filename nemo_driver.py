from nemo_api import NemoAPI
from stock_brocker_driver_interface import StockerBrockerDriverInterface


class NemoDriver(StockerBrockerDriverInterface):
    def __init__(self):
        self.__nemo_api = NemoAPI()

    def login(self, id, passwd):
        self.__nemo_api.cerification(id, passwd)

    def buy(self, code, quantity, price):
        self.__nemo_api.purchasing_stock(code, price, quantity)

    def sell(self, code, quantity, price):
        self.__nemo_api.selling_stock(code, price, quantity)

    def get_price(self, code):
        self.__nemo_api.get_market_price(code, 0)
