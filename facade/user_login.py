from config.config_helper import ConfigHelper
import hashlib


class UserLoginFacade:

    def __init__(self, cfg: ConfigHelper):
        self.__username = cfg.config['auth']['username']
        self.__password_hash = cfg.config['auth']['password']

    def authenticate_user(self, username, password):

        encryptor = hashlib.sha256()
        encryptor.update(str.encode(password))

        password_encrypted = encryptor.hexdigest()

        return username == self.__username and password_encrypted == self.__password_hash
