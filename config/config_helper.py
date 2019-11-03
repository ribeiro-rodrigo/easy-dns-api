import configparser


class ConfigHelper:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.__config = parser

    @property
    def config(self):
        return self.__config

