from injector import provider, singleton
from flask_injector import Module

from services.dns import DNSService
from services.auth import AuthService

from config.config_helper import ConfigHelper


class ServiceModule(Module):

    @provider
    @singleton
    def provide_dns_service(self, config: ConfigHelper) -> DNSService:
        return DNSService(config)

    @provider
    @singleton
    def provide_auth_service(self, config: ConfigHelper) -> AuthService:
        return AuthService(config)


__all__ = ['ServiceModule']