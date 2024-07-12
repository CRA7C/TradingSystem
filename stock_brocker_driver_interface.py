class StockerBrockerDriverInterface:

    def __init__(self):
        raise TypeError


    def login(self, id, passwd):
        pass

    def buy(self, code, quantity, price):
        pass

    def sell(self, code, quantity, price):
        pass

    def get_price(self,code):
        pass
