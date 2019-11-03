from config.config_helper import ConfigHelper
from services.dns import DNSService


class DNSRecordsFacade:
    def __init__(self, dns_service: DNSService, config_helper: ConfigHelper):
        self.__avaliable_zones = config_helper.avaliable_zones
        self.__dns_service = dns_service

    def insert_record(self, record: dict):

        if not self.__is_valid_domain(record["recordName"]):
            raise InvalidZone("'zone' not enabled")

        self.__dns_service.add_record(record)

    def __is_valid_domain(self, record_name):
        return list(
            filter(lambda domain: record_name.endswith(domain), self.__avaliable_zones)
        )


class InvalidZone(Exception):
    pass
