from services.dns import DNSService
from models.record import Record


class DNSRecordsFacade:
    def __init__(self, dns_service: DNSService):
        self.__dns_service = dns_service

    def insert_record(self, record: Record):

        DNSRecordsFacade.__check_zone(record)
        return self.__dns_service.add_record(record)

    def delete_record(self, record: Record):

        DNSRecordsFacade.__check_zone(record)
        return self.__dns_service.delete_record(record)

    @classmethod
    def __check_zone(cls, record: Record):
        if not record.is_valid_zone():
            raise InvalidZone("'zone' not enabled")


class InvalidZone(Exception):
    pass
