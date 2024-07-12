from abc import ABC, abstractmethod


class StockerBrokerDriverInterface(ABC):
    @abstractmethod
    def login(self, id, passwd):
        pass

    @abstractmethod
    def buy(self, code, quantity, price):
        pass

    @abstractmethod
    def sell(self, code, quantity, price):
        pass

    @abstractmethod
    def get_price(self, code):
        pass
