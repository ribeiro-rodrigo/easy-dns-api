from injector import provider, singleton
from flask_injector import Module

from services.dns import DNSService
from config.config_helper import ConfigHelper


class ServiceModule(Module):

    @provider
    @singleton
    def provide_dns_service(self, config: ConfigHelper) -> DNSService:
        return DNSService(config)


__all__ = ['ServiceModule']