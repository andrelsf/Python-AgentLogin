from util.entity.pyconfigloader import ConfigLoader 

class Queue:

    def __init__(self):
        self.__get_config = ConfigLoader()
        self.__queue = self.__get_config.get_queue()

    def get_queue(self):
        return self.__queue