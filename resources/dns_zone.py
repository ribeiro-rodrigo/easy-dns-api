from flask_restful import Resource
from services.dns import DNSService

from injector import inject


class DNSZone(Resource):

    @inject
    def __init__(self, dns_service: DNSService):
        self.__dns_service = dns_service

    def get(self):
        pass


