import configparser
import ast


class ConfigHelper:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.__config = parser

    @property
    def config(self):
        return self.__config

    @property
    def avaliable_zones(self):
        return ast.literal_eval(self.__config.get('dns', 'avaliable_zones'))

