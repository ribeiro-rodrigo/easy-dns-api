from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector

from resources.dns_record import DNSRecord
from resources.dns_zone import DNSZone
from resources.dns_all_records import DNSAllRecords

from services import ServiceModule
from config import ConfigModule
from facade import FacadeModule

app = Flask(__name__)
api = Api(app)

api.add_resource(DNSZone, '/v1/dns/zone')
api.add_resource(DNSAllRecords, '/v1/dns/records')
api.add_resource(DNSRecord, '/v1/dns/record/<string:record_name>/type/<string:record_type>')

FlaskInjector(app=app, modules=[
    ServiceModule,
    ConfigModule,
    FacadeModule,
])

if __name__ == '__main__':
    debug_mode = True
    app.run(debug=debug_mode)

