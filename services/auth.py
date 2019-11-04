from flask_jwt_extended import create_access_token
import datetime

from config.config_helper import ConfigHelper


class AuthService:

    def __init__(self, cfg: ConfigHelper):
        self.__token_expires = cfg.token_expires

    def generate_token(self, username):
        expires = datetime.timedelta(minutes=self.__token_expires)
        access_token = create_access_token(identity=username, expires_delta=expires)
        return access_token
