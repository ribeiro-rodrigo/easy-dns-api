from flask_restful import Resource

from facade.dns import DNSFacade


class DNSRecord(Resource):

    def __init__(self, dns_facade: DNSFacade):
        self.__dns_facade = dns_facade

    def put(self, record_name, record_type):
        pass

    def delete(self, record_name, record_type):
        pass

