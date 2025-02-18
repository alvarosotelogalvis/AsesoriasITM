from project.app.professors.domain.ports.professorsPort import (
    professorPort
)

class CreateprofessorService:

    def __init__(
        self,
        professor_port: professorPort
    ):
        self.professor_port = professor_port

    def execute(self, **kwargs):
        # Validation
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

    def __validate_professor(self, identification_card: int):
        get_profesor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if get_profesor:
            raise Exception("The professor is already registered")
