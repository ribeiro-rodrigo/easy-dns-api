from services.dns import DNSService
from models.record import Record


class DNSRecordsFacade:
    def __init__(self, dns_service: DNSService):
        self.__dns_service = dns_service

    def insert_record(self, record: Record):

        if not record.is_valid_zone():
            raise InvalidZone("'zone' not enabled")

        self.__dns_service.add_record(record)


class InvalidZone(Exception):
    pass
