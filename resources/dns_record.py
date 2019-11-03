from flask_restful import Resource

from facade.dns_zones import DNSZonesFacade


class DNSRecord(Resource):

    def __init__(self, dns_facade: DNSZonesFacade):
        self.__dns_facade = dns_facade

    def put(self, record_name, record_type):
        pass

    def delete(self, record_name, record_type):
        pass

