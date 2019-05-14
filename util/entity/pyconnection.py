from util.entity.pyconfigloader import ConfigLoader

class Connection:

    def __init__(self):
        self.__get_datas_connection = ConfigLoader()
        self.__host, self.__port, self.__vhost, self.__user, self.__password = self.__get_datas_connection.get_connection()
        
    def get_host(self):
        return self.__host
    
    def get_port(self):
        return self.__port
    
    def get_vhost(self):
        return self.__vhost

    def get_user(self):
        return self.__user

    def get_password(self):
        return self.__password
    