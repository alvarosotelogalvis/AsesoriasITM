from project.app.professors.domain.ports.professorsPort import (
    professorPort
)
from project.app.users.domain.ports.userPort import UserPort

class SignUpService:

    def __init__(
        self,
        professor_port: professorPort,
        user_port: UserPort
    ):
        self.professor_port = professor_port
        self.user_port = user_port

    def execute(
        self,
        institutional_email: str,
        identification_card: int,
        password: str
    ):
        # Validations
        professor = self.__validate_professor(
            institutional_email=institutional_email,
            identification_card=identification_card
        )
        self.__validate_logged_in_users(
            institutional_email=institutional_email
        )
        
        # create a user to login
        create_user = self.user_port.create_user(
            **{
                "institutional_email": institutional_email,
                "professor_id": professor.id,
                "password": password
            }
        )
        if create_user is None:
            raise Exception("Logged-in user could not be created")
        return {"successful": "User successfully logged in"}

    def __validate_professor(
        self,
        institutional_email: str,
        identification_card: int
    ):
        get_professor = self.professor_port.get_professor(
            **{
                "institutional_email": institutional_email,
                "identification_card": identification_card
            }
        )
        if not get_professor:
            raise Exception("The email or ID number is incorrect.")
        return get_professor

    def __validate_logged_in_users(
        self,
        institutional_email: str
    ):
        get_user = self.user_port.get_user_by_username(
            username=institutional_email
        )
        if get_user:
            raise Exception("The user has already set a password. Use the login.")
