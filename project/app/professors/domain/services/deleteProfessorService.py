from project.app.professors.domain.config.permittedRoles import (
    permitted_roles_for_teachers
)
from project.app.professors.domain.ports.professorsPort import (
    professorPort
)
from project.app.users.domain.ports.userPort import UserPort

class DeleteprofessorService:

    def __init__(
        self,
        professor_port: professorPort,
        user_port: UserPort
    ):
        self.professor_port = professor_port
        self.user_port = user_port

    def execute(
        self,
        role_name: str,
        identification_card: int
    ):
        # Validations
        self.__validate_role(role_name=role_name)
        professor = self.__validate_professor(
            identification_card=identification_card
        )
        is_loggedin_user = self.__validate_loggedin_user(
            username=professor.institutional_email
        )
        # Delete professor from the professors table
        self.professor_port.delete_professor(
            identification_card=identification_card
        )
        # Delete Professor from the logged-in_users table
        if is_loggedin_user:
            self.user_port.delete_user(
                professor_id=professor.id
            )
        return {"successful": "The professor was deleted correctly"}

    def __validate_role(self, role_name: str):
        if role_name not in permitted_roles_for_teachers:
            raise Exception(
                "The user does not have permissions to perform this action.")

    def __validate_professor(self, identification_card: int):
        get_professor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if not get_professor:
            raise Exception("The professor is not registered")
        return get_professor

    def __validate_loggedin_user(self, username: str):
        get_user = self.user_port.get_user_by_username(
            username=username
        )
        return get_user != None
