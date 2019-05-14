# -*- coding: utf-8 -*-

from locale import setlocale, Error, LC_ALL

class Locale():

    def __init__(self):
        try:
            setlocale(LC_ALL, 'pt_BR.UTF-8')
        except Error as err:
            print(err)
        else:
            print("[ INFO ] Setting Locale.")