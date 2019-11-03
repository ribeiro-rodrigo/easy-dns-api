from flask_injector import Module
from injector import provider, singleton

from config.config_helper import ConfigHelper


class ConfigModule(Module):

    @provider
    @singleton
    def provide_config(self) -> ConfigHelper:
        return ConfigHelper()
