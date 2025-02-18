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
        identification_card: int
    ):
        # Validation
        self.__validate_professor(identification_card=identification_card)
        self.professor_port.delete_professor(
            identification_card=identification_card
        )
        return {"successful": "The professor was deleted correctly"}

    def __validate_professor(self, identification_card: int):
        get_profesor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if not get_profesor:
            raise Exception("The professor is not registered")
