from flask_injector import Module
from injector import provider, singleton

from services.dns import DNSService
from config.config_helper import ConfigHelper

from facade.dns_zones import DNSZonesFacade
from facade.dns_records import DNSRecordsFacade
from facade.user_login import UserLoginFacade


class FacadeModule(Module):

    @provider
    @singleton
    def provide_dns_zones(self, dns_service: DNSService, config_helper: ConfigHelper) -> DNSZonesFacade:
        return DNSZonesFacade(dns_service, config_helper)

    @provider
    @singleton
    def provide_dns_records(self, dns_service: DNSService) -> DNSRecordsFacade:
        return DNSRecordsFacade(dns_service)

    @provider
    @singleton
    def provide_user_login(self, config_helper: ConfigHelper) -> UserLoginFacade:
        return UserLoginFacade(config_helper)


