from flask_restful import Resource
from injector import inject

from facade.dns_records import DNSRecordsFacade, InvalidZone
from models.record import Record
from config.config_helper import ConfigHelper


class DNSRecord(Resource):

    @inject
    def __init__(self, dns_records_facade: DNSRecordsFacade, cfg: ConfigHelper):
        self.__dns_records_facade = dns_records_facade
        self.__avaliable_zones = cfg.avaliable_zones

    def put(self, record_name, record_type):
        pass

    def delete(self, zone_name, record_name):

        try:

            record = Record({"recordName": record_name}, zone_name, self.__avaliable_zones)
            removed = self.__dns_records_facade.delete_record(record)

            if not removed:
                return {"message": "could not remove entry in DNS record", "errors": []}, 422

            return None, 204

        except InvalidZone as e:
            return {"message": "not authorized", "errors": [str(e)]}, 422

        except Exception as e:
            print(str(e))
            return {"message": "internal error"}, 500