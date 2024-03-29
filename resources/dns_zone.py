from flask_restful import Resource
from flask_jwt_extended import jwt_required
from injector import inject

from facade.dns_zones import DNSZonesFacade


class DNSZone(Resource):

    @inject
    def __init__(self, dns_facade: DNSZonesFacade):
        self.__dns_facade = dns_facade

    @jwt_required
    def get(self):

        try:

            all_zones = self.__dns_facade.list_all_zones()
            return all_zones, 200

        except Exception as e:

            return {"message": str(e)}, 500



