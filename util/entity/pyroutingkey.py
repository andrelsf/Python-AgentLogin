# -*- coding: utf-8 -*-

from util.entity.pyconfigloader import ConfigLoader

class RoutingKey():

    def __init__(self):
        self.__config_loader = ConfigLoader()
        self.__routing_key = self.__config_loader.get_routing_key()

    def get_routing_key(self):
        return self.__routing_key