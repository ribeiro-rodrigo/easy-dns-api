from flask_restful import Resource, request
from injector import inject
from resources.validators.dns_record import DNSRecordJSONValidator

from facade.dns_records import DNSRecordsFacade, InvalidZone
from models.record import Record
from config.config_helper import ConfigHelper


class DNSAllRecords(Resource):

    @inject
    def __init__(self, dns_records_facade: DNSRecordsFacade, cfg: ConfigHelper):
        self.__dns_records_facade = dns_records_facade
        self.__avaliable_zones = cfg.avaliable_zones

    def post(self, zone_name):

        json_validator = DNSRecordJSONValidator(request)

        if not json_validator.validate():
            return {"message": "validation error", "errors": json_validator.errors}, 422

        try:

            record_dto = request.json
            record = Record(record_dto, zone_name, self.__avaliable_zones)
            added = self.__dns_records_facade.insert_record(record)

            if not added:
                return {"message": "could not insert entry in DNS record", "errors": []}, 422

            return "", 201, {
                'Location': f'{request.path}/{record.full_name}/type/{record.type}'
            }

        except InvalidZone as e:
            return {"message": "not authorized", "errors": [str(e)]}, 422

        except Exception:
            return {"message": "internal error"}, 500






