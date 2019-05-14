# -*- coding: utf-8 -*-

from os import getlogin, uname
from platform import system, node, release, version
from time import strftime

class Login():

    def __init__(self):
        self._date = strftime("%d-%m-%Y %H:%M:%S")
        self._login = getlogin()
        self._sysname = system()
        self._nodename = node()
        self._kernel = release() + " " + version()

    def get_login_user(self):
        return self._login, self._sysname, self._nodename, self._date, self._kernel

# user = Login()
# login, sys_name, node_name, date = user.get_login_user()
# print(login, ":", sys_name, ":", node_name, ":", date)
