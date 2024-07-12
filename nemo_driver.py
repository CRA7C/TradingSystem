from nemo_api import NemoAPI


class NemoDriver():
    def __init__(self):
        self.__nemo_api = NemoAPI()

    def login(self, id, pw):
        self.__nemo_api.cerification(id, pw)

    def buy(self, code, price, quantity):
        self.__nemo_api.purchasing_stock(code, price, quantity)

    def sell(self, code, price, quantity):
        self.__nemo_api.selling_stock(code, price, quantity)

    def get_price(self, code):
        self.__nemo_api.get_market_price(code, 0)
