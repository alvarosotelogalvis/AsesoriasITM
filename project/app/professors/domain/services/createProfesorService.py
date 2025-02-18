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
        create_professor = self.professor_port.create_professor(**kwargs)
        if not create_professor:
            raise Exception("The professor could not be created")
