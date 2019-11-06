import configparser
import ast
import os


class ConfigHelper:
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')
        self.__config = parser


    @property
    def server_host(self):
        return os.environ.get('DNS_SERVER_HOST', None) or self.__config.get('dns', 'server_host')

    @property
    def tsig_key(self):
        return os.environ.get('TSIG_KEY', None) or self.__config.get('tsig', 'key')

    @property
    def auth_username(self):
        return os.environ.get('AUTH_USERNAME', None) or self.__config.get('auth', 'username')

    @property
    def auth_password(self):
        return os.environ.get('AUTH_PASSWORD', None) or self.__config.get('auth', 'password')

    @property
    def avaliable_zones(self):
        return ast.literal_eval(os.environ.get('DNS_AVALIABLE_ZONES', "None")) or \
               ast.literal_eval(self.__config.get('dns', 'avaliable_zones'))

    @property
    def connection_timeout(self):
        return float(os.environ.get('DNS_CONNECTION_TIMEOUT', 0.0)) or \
               float(self.__config.get('dns', 'connection_timeout'))

    @property
    def token_expires(self):
        return int(os.environ.get('AUTH_TOKEN_EXPIRES_IN_MINUTES', 0)) or \
               int(self.__config.get('auth', 'token_expires_in_minutes'))

