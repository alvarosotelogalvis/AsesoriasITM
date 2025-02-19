from project.app.professors.domain.config.permittedRoles import (
    permitted_roles_for_teachers
)
from project.app.professors.domain.ports.professorsPort import (
    professorPort
)

class DeleteprofessorService:

    def __init__(
        self,
        professor_port: professorPort
    ):
        self.professor_port = professor_port

    def execute(
        self,
        role_name: str,
        identification_card: int
    ):
        # Validations
        self.__validate_role(role_name=role_name)
        self.__validate_professor(identification_card=identification_card)
        # Delete professor
        self.professor_port.delete_professor(
            identification_card=identification_card
        )
        return {"successful": "The professor was deleted correctly"}

    def __validate_role(self, role_name: str):
        if role_name not in permitted_roles_for_teachers:
            raise Exception(
                "The user does not have permissions to perform this action.")

    def __validate_professor(self, identification_card: int):
        get_profesor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if not get_profesor:
            raise Exception("The professor is not registered")
