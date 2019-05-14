from yaml import load
from os import getcwd, path

class ConfigLoader():

    def __init__(self):
        self.__current_dir = getcwd()
        self.__config_file = self.__current_dir + "/data/config.d/agentlogin.yaml"

    def get_routing_key(self):
        try:
            datas = self.__config_loader()
            rabbitmq = datas.get('rabbitmq')
            agent_login = rabbitmq.get('agentlogin')
            routing_key = agent_login.get('routing_key')
        except TypeError as err:
            print("[ ERROR ] :", err)
            return False
        except AttributeError as err:
            print("[ ERROR ] :", err)
            return False
        except KeyError as err:
            print("[ ERROR ] :", err)
            return False
        else:
            return routing_key


    def get_queue(self):
        try:
            datas = self.__config_loader()
            rabbitmq = datas.get('rabbitmq')
            agent_login = rabbitmq.get('agentlogin')
            queue = agent_login.get('queue')
            queue_name = queue[0]['queue']
        except TypeError as err:
            print("[ ERROR ] :", err)
            return False
        except AttributeError as err:
            print("[ ERROR ] :", err)
            return False
        except KeyError as err:
            print("[ ERROR ] :", err)
            return False
        else:
            return queue_name


    def get_exchange(self):
        try:
            datas = self.__config_loader()
            rabbitmq = datas.get('rabbitmq')
            agent_login = rabbitmq.get('agentlogin')
            exchange = agent_login.get('exchange')
            exchange_name = exchange[0]['exchange']
            exchange_type = exchange[0]['exchange_type']
            durable = exchange[0]['durable']
        except TypeError as err:
            print("[ ERROR ] :", err)
            return False
        except AttributeError as err:
            print("[ ERROR ] :", err)
            return False
        except KeyError as err:
            print("[ ERROR ] :", err)
            return False
        else:
            return exchange_name, exchange_type, durable


    def get_connection(self):
        try:
            datas = self.__config_loader()
            rabbitmq = datas.get("rabbitmq")
            agent_login = rabbitmq.get('agentlogin')
            connection = agent_login.get('connection')
            host = connection[0]['host']
            port = connection[0]['port']
            vhost = connection[0]['vhost']
            user = connection[0]['user']
            password = connection[0]['pass']
        except TypeError as err:
            print("[ ERROR ] :", err)
            return False
        except AttributeError as err:
            print("[ ERROR ] :", err)
            return False
        except KeyError as err:
            print("[ ERROR ] :", err)
            return False
        else:
            return host, port, vhost, user, password


    def __config_loader(self):
        try:
            if (path.exists(self.__config_file)):
                with open(self.__config_file, 'r') as yaml_file:
                    datas = load(yaml_file)
                return datas
        except PermissionError as err:
            print("[ ERROR ] :", err)
            return False
        except FileNotFoundError as err:
            print("[ ERROR ] :", err)
            return False
        except FileExistsError as err:
            print("[ ERROR ] :", err)
            return False
        except:
            print("[ ERROR ] : Unknown")
            return False
