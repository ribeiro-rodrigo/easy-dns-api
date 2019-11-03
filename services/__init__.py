from injector import provider, singleton
from flask_injector import Module

from services.dns import DNSService


class ServiceModule(Module):

    @provider
    @singleton
    def provide_dns_service(self) -> DNSService:
        return DNSService()


__all__ = ['ServiceModule']