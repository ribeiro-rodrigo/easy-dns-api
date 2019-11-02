from flask_restful import Resource


class DNSRecord(Resource):

    def get(self, zone_name, record_name, record_type):
        pass

    def put(self, zone_name, record_name, record_type):
        pass

    def delete(self, zone_name, record_name, record_type):
        pass

