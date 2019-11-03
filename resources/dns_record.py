from flask_restful import Resource, request
from injector import inject

from facade.dns_records import DNSRecordsFacade, InvalidZone, RecordNotExists
from models.record import Record
from resources.validators.dns_record import DNSRecordJSONValidator
from config.config_helper import ConfigHelper


class DNSRecord(Resource):

    @inject
    def __init__(self, dns_records_facade: DNSRecordsFacade, cfg: ConfigHelper):
        self.__dns_records_facade = dns_records_facade
        self.__avaliable_zones = cfg.avaliable_zones

    def put(self, zone_name, record_name):

        request.json['recordName'] = record_name

        json_validator = DNSRecordJSONValidator(request)

        if not json_validator.validate():
            return {"message": "validation error", "errors": json_validator.errors}, 422

        record_dto = request.json
        record = Record(record_dto, zone_name, self.__avaliable_zones)

        try:

            updated = self.__dns_records_facade.update_record(record)

            if not updated:
                return {"message": "could not update entry in DNS record", "errors": []}, 422

            return None, 204

        except InvalidZone as e:
            return {"message": "not authorized", "errors": [str(e)]}, 422

        except RecordNotExists:
            return {"message": "record not exists", "errors": []}, 404

        except Exception as e:
            print(str(e))
            return {"message": "internal error"}, 500

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