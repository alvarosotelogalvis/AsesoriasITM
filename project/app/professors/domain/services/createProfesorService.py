from project.app.professors.domain.config.permittedRoles import (
    permitted_roles_for_teachers
)
from project.app.professors.domain.ports.professorsPort import (
    professorPort
)

class CreateprofessorService:

    def __init__(
        self,
        professor_port: professorPort
    ):
        self.professor_port = professor_port

    def execute(self, role_name: str, **kwargs):
        # Validations
        self.__validate_role(role_name=role_name)
        self.__validate_professor(
            identification_card=kwargs.get("identification_card")
        )
        create_professor = self.professor_port.create_professor(**kwargs)
        if not create_professor:
            raise Exception("The professor could not be created")
        return {
            "id": create_professor.id,
            "fullname": create_professor.fullname,
        }

    def __validate_role(self, role_name: str):
        if role_name not in permitted_roles_for_teachers:
            raise Exception(
                "The user does not have permissions to perform this action.")

    def __validate_professor(self, identification_card: int):
        get_profesor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if get_profesor:
            raise Exception("The professor is already registered")
