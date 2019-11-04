from flask_restful import Resource
from flask_injector import inject
from flask_jwt_extended import jwt_refresh_token_required, get_jwt_identity

from services.auth import AuthService


class RefreshLogin(Resource):

    @inject
    def __init__(self, auth_service: AuthService):
        self.__auth_service = auth_service

    @jwt_refresh_token_required
    def post(self):

        token = self.__auth_service.generate_token(get_jwt_identity())

        return {"access_token": token}, 200






