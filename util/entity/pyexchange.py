
from util.entity.pyconfigloader import ConfigLoader

class Exchange():

    def __init__(self):
        self.__get_exchange = ConfigLoader()
        self.__exchange_name, self.__exchange_type, self.__durable = self.__get_exchange.get_exchange()

    def get_exchange_name(self):
        return self.__exchange_name

    def get_exchange_type(self):
        return self.__exchange_type

    def get_exchange_durable(self):
        return self.__durable