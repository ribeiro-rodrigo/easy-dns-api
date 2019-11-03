from flask_restful import Resource, request
from injector import inject
from resources.validators.dns_record import DNSRecordJSONValidator

from facade.dns_records import DNSRecordsFacade, InvalidZone


class DNSAllRecords(Resource):

    @inject
    def __init__(self, dns_records_facade: DNSRecordsFacade):
        self.__dns_records_facade = dns_records_facade

    def post(self):

        json_validator = DNSRecordJSONValidator(request)

        if not json_validator.validate():
            return {"message": "validation error", "errors": json_validator.errors}, 422

        try:

            record = request.json
            self.__dns_records_facade.insert_record(record)

            return "", 201, {
                'Location': f'{request.path}/{record["recordName"]}/type/{record["recordType"]}'
            }

        except InvalidZone as e:
            return {"message": "not authorized", "errors": [str(e)]}, 422






