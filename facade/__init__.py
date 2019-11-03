from flask_injector import Module
from injector import provider, singleton

from services.dns import DNSService
from config.config_helper import ConfigHelper
from facade.dns import DNSFacade


class FacadeModule(Module):

    @provider
    @singleton
    def provide_dns_facade(self, dns_service: DNSService, config_helper: ConfigHelper) -> DNSFacade:
        return DNSFacade(dns_service, config_helper)


