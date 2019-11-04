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

    @property
    def connection_timeout(self):
        return float(self.__config.get('dns', 'connection_timeout'))

    @property
    def token_expires(self):
        return int(self.__config.get('auth', 'token_expires_in_minutes'))

