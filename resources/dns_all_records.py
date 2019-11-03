from flask_restful import Resource, request
from resources.validators.dns_record import DNSRecordJSONValidator


class DNSAllRecords(Resource):

    def post(self):

        json_validator = DNSRecordJSONValidator(request)

        if not json_validator.validate():
            return {"message": "validation error", "errors": json_validator.errors}, 422

        record = request.json

        valid_domain = filter(lambda domain: record["recordName"].endswith(domain), ["test.example.com"])

        if not valid_domain:
            return {"message": "not authorized", "errors": ["'zone' not enabled"]}, 422

        return "", 201, {'Location': f'{request.path}/{record["recordName"]}/type/{record["recordType"]}'}





