# -*- coding: utf-8 -*-

import pika
from os import sys, getcwd
from base64 import b64decode
from util.entity.pyconnection import Connection
from util.entity.pyexchange import Exchange
from util.entity.pyqueue import Queue
from util.entity.pyroutingkey import RoutingKey

class AgentSender():

    def __init__(self, message):
        self.__cache_file = getcwd() + "/data/cache/messages"
        self.__message = message
        """
            Busca as informações de conexões
        """
        self.__connections = Connection()
        self.__host = self.__connections.get_host() 
        self.__port = self.__connections.get_port()
        self.__vhost = self.__connections.get_vhost()
        self.__user = self.__connections.get_user()
        self.__password = b64decode(bytes("{}".format(self.__connections.get_password()), 'utf-8'))
        """
            Busca as informações do Exchange.
        """
        self.__get_exchange = Exchange()
        self.__exchange_name = self.__get_exchange.get_exchange_name()
        self.__exchange_type = self.__get_exchange.get_exchange_type()
        self.__durable = self.__get_exchange.get_exchange_durable()
        """
            Busca as informações da Queue.
        """
        self.__get_queue = Queue()
        self.__queue  = self.__get_queue.get_queue()
        """
            Busca informação da routing_key.
        """
        self.__get_routing_key = RoutingKey()
        self.__routing_key = b64decode(bytes("{}".format(self.__get_routing_key.get_routing_key()), 'utf-8'))
        """
           Inicia o processo de conexão com RabbitMQ
        """
        self.__credentials = pika.PlainCredentials(self.__user, self.__password)
        try:
            self.__connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=self.__host,
                    port=self.__port,
                    virtual_host=self.__vhost,
                    credentials=self.__credentials
                )
            )
            self.__channel = self.__connection.channel()
            self.__channel.exchange_declare(
                exchange=self.__exchange_name,
                exchange_type=self.__exchange_type,
                durable=True
                )
            self.__result = self.__channel.queue_declare(
                queue=self.__queue
            )
            self.__channel.queue_bind(
                exchange=self.__exchange_name,
                queue=self.__result.method.queue
            )
        except pika.exceptions.AMQPConnectionError as err:
            print("[ ERROR ] :", err)
            self.__save_menssage_local(self.__message)
        except pika.exceptions.AMQPError as err:
            print("[ ERROR ] :", err)
            self.__save_menssage_local(self.__message)
        except pika.exceptions.AMQPChannelError as err:
            print("[ ERROR ] :", err)
            self.__save_menssage_local(self.__message)
        except pika.exceptions.AuthenticationError as err:
            print("[ ERROR ] :", err)
            self.__save_menssage_local(self.__message)
        except TypeError as err:
            print("[ ERROR ] :", err)
            self.__save_menssage_local(self.__message)
        else:
            print("[ INFO ] Connection to RabbitMQ Successfully.")
            self.__publish_message(self.__message)
        self.__verify_cache_messages()


    def __publish_message(self, message):
        try:
            self.__channel.basic_publish(
                exchange=self.__exchange_name,
                routing_key=self.__routing_key,
                body=message
            )
        except pika.exceptions.BodyTooLongError as err:
            print("[ ERROR ] :", err)
            return False
        else:
            print("[X] Sent message to RabbitMQ")
            return True


    def __verify_cache_messages(self):
        """
            Ao realizar um novo login e efetivar o envio para
            o RMQ, este metodo realiza a verificação do arquivo
            de cache para enviar mensagens pendentes.
        """
        try:
            with open(self.__cache_file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    content = line.split(";")
                    if not (self.__publish_message(message=content)):
                        print("[ ERROR ] : Falha ao enviar mensagem em cache. Saindo do programa.")
                        sys.exit(1)
            with open(self.__cache_file, 'w') as f:
                f.write("")
        except FileNotFoundError as err:
            print("[ ERROR ]:", err)
        except PermissionError as err:
            print("[ ERROR ]:", err)


    def __save_menssage_local(self, message):
        """
            Em caso de erro ao enviar a mensagem para o RMQ
            e realizado o cache das mensagens não enviadas.
        """
        try:
            with open(self.__cache_file, 'a') as f:
                f.write(message + ";1\n")
        except FileNotFoundError as err:
            print("[ ERROR ]:", err)
        except PermissionError as err:
            print("[ ERROR ]:", err)
