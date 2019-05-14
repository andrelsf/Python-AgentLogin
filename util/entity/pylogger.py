import logging
from os import getcwd, path

class Logger():

    def __init__(self):
        self.__LOG_FORMAT = "%(asctime)s %(levelname)s [%(funcName)s]: %(message)s"
        try:
            log_file = getcwd() + "/data/log/agentlogin.log"
            logging.basicConfig(
                filename=log_file,
                level=logging.INFO,
                format=self.__LOG_FORMAT,
                filemode='a'
            )
        except FileNotFoundError as err:
            print("[ ERROR ]:", err)
            return False
        except PermissionError as err:
            print("[ ERROR ]:", err)
            return False
        except AttributeError as err:
            print("[ ERROR ]:", err)
            return False
        else:
            self.__logger = logging.getLogger()

    def info(self, message):
        self.__logger.info(message)
    
    def error(self, message):
        self.__logger.error(message)

    def warnning(self, message):
        self.__logger.warning(message)