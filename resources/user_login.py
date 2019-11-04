from flask_restful import Resource, request
from flask_injector import inject

from facade.user_login import UserLoginFacade
from services.auth import AuthService


class UserLogin(Resource):

    @inject
    def __init__(self, user_login_facade: UserLoginFacade, auth_service: AuthService):
        self.__user_login_facade = user_login_facade
        self.__auth_service = auth_service

    def post(self):

        user_dto = request.json

        authenticated = self.__user_login_facade.authenticate_user(
            user_dto['username'], user_dto['password']
        )

        if not authenticated:
            return {"message": "user not authenticated"}, 401

        access_token, refresh_token = self.__auth_service.generate_access_and_refresh_token(
            user_dto['username']
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }, 200






