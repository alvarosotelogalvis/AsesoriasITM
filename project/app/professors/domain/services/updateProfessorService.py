from project.app.professors.domain.ports.professorsPort import (
    professorPort
)

class UpdateprofessorService:

    def __init__(
        self,
        professor_port: professorPort
    ):
        self.professor_port = professor_port
    
    def execute(self, **kwargs):
        identification_card = kwargs.get("identification_card")
        # Validation
        self.__validate_professor(identification_card=identification_card)
        # Update Professor
        kwargs.pop("identification_card")
        update_professor = self.professor_port.update_professor(
            identification_card=identification_card,
            **kwargs
        )
        return {"successful": "The professor was updated correctly"}

    def __validate_professor(self, identification_card: int):
        get_profesor = self.professor_port.get_professor_by_identification_card(
            identification_card=identification_card
        )
        if not get_profesor:
            raise Exception("The professor is not registered")
