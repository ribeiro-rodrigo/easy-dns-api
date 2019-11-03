from flask_restful import Resource
from injector import inject

from facade.dns import DNSFacade


class DNSZone(Resource):

    @inject
    def __init__(self, dns_facade: DNSFacade):
        self.__dns_facade = dns_facade

    def get(self):

        try:

            all_zones = self.__dns_facade.list_all_zones()
            return all_zones, 200

        except Exception as e:

            return {"message": str(e)}, 500



