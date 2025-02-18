from project.app.users.entrypoints.serializers.signInSerializer import (
    SignInSerializer
)
from project.app.users.domain.ports.userPort import UserPort

from flask_jwt_extended import create_access_token, create_refresh_token


class SignInService:

    def __init__(
        self,
        user_port: UserPort
    ):
        self.user_port = user_port

    def execute(
        self,
        username: str,
        password: str
    ):
        user = self.user_port.get_user_by_username(
            username=username
        )
        if user and user.check_password(password):
            user = SignInSerializer().dump(user)
            access_token = create_access_token(identity=user, fresh=True)
            refresh_token = create_refresh_token(identity=user)
            user.pop("professor_id")
            return {
                'auth': {
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'user': user
                },
                'cookies': None
            }
        raise Exception(f"incorrect username or password")
