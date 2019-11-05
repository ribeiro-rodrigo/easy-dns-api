from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector
from flask_jwt_extended import JWTManager

from resources.dns_record import DNSRecord
from resources.dns_zone import DNSZone
from resources.dns_all_records import DNSAllRecords
from resources.user_login import UserLogin
from resources.refresh_login import RefreshLogin

from services import ServiceModule
from config import ConfigModule
from facade import FacadeModule
import os

app = Flask(__name__)

JWT_SECRET = os.environ.get('JWT_SECRET ', None)
app.config['JWT_SECRET_KEY'] = JWT_SECRET if JWT_SECRET else 'easy-dns-api-secret'

api = Api(app)

api.add_resource(DNSZone, '/v1/dns/zones')
api.add_resource(DNSAllRecords, '/v1/dns/zones/<string:zone_name>/records')
api.add_resource(DNSRecord, '/v1/dns/zones/<string:zone_name>/records/<string:record_name>')
api.add_resource(UserLogin, '/auth')
api.add_resource(RefreshLogin, '/refresh')

JWTManager(app)

FlaskInjector(app=app, modules=[
    ServiceModule,
    ConfigModule,
    FacadeModule,
])

if __name__ == '__main__':

    port = int(os.environ.get('SERVER_PORT')) if os.environ.get('SERVER_PORT', None) else 5000 
    debug_mode = False if os.environ.get('ENVIRONMENT',None) else True  
    app.run("0.0.0.0",debug=debug_mode, port=port)

