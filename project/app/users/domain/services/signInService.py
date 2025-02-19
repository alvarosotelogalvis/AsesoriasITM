from project.app.professors.domain.ports.professorsPort import (
    professorPort
)
from project.app.users.entrypoints.serializers.signInSerializer import (
    SignInSerializer
)
from project.app.users.domain.ports.userPort import UserPort

from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
import json


class SignInService:

    def __init__(
        self,
        user_port: UserPort,
        professor_port: professorPort
    ):
        self.user_port = user_port
        self.professor_port = professor_port

    def execute(
        self,
        username: str,
        password: str
    ):
        user = self.user_port.get_user_by_username(
            username=username
        )
        if not user:
            raise Exception(f"The professor must create the password or incorrect username")
        elif not user.check_password(password):
            raise Exception(f"Incorrect password")
        get_professor = self.professor_port.get_professor_by_id(
            professor_id=user.professor_id
        )
        user = SignInSerializer().dump(get_professor)
        access_token = create_access_token(identity=json.dumps(user), fresh=True)
        refresh_token = create_refresh_token(identity=user)
        access_token_exp = datetime.fromtimestamp(
            decode_token(access_token).get('exp')
        ).strftime('%Y-%m-%d %H:%M:%S')
        return {
            'auth': {
                'access_token': access_token,
                'refresh_token': refresh_token,
                'access_token_exp': access_token_exp,
                'user': user
            },
            'cookies': None
        }
