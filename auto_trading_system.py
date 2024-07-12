from stock_brocker_driver_interface import StockerBrockerDriverInterface

class AutoTradingSystem:
    def __init__(self):
        self.brocker = None

    def select_stock_brocker(self, param):
        if param not in ['kiwer', 'nemo']:
            raise ValueError(f"{param} stock brocker does not exist.")

        
    def login(self, id, password):
        self.brocker.login(id, password)

    def buy(self, code, price, quantity):
        self.brocker.buy(code, price, quantity)

    def sell(self, code, price, quantity):
        self.brocker.sell(code, price, quantity)

    def get_price(self, code):
        return self.brocker.get_price(code)



