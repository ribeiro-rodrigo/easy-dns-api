from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector

from resources.dns_record import DNSRecord
from resources.dns_zone import DNSZone

from services import ServiceModule

app = Flask(__name__)
api = Api(app)

api.add_resource(DNSZone, '/v1/dns/zone')
api.add_resource(DNSRecord, '/v1/dns/zone/<zone_name>/record/<record_name>/type/<record_type>')

FlaskInjector(app=app, modules=[ServiceModule])

if __name__ == '__main__':
    debug_mode = True
    app.run(debug=debug_mode)

