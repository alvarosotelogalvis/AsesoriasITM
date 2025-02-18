from project.app.professors.domain.models.professorsModel import (
    professorModel
)
from project.shared.config.database import SessionFactory

from sqlalchemy import update
from sqlalchemy.orm.exc import FlushError
from injector import inject

class professorAdapter:

    @inject
    def __init__(self):
        self.session = SessionFactory

    def get_professor(self, **kwargs):
        try:
            professor = self.session.query(
                professorModel
            ).filter(
                professorModel.institutional_email == kwargs.get("institutional_email"),
                professorModel.identification_card == kwargs.get("identification_card")
            ).first()
            return professor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()

    def get_professor_by_identification_card(
        self,
        identification_card: int
    ):
        try:
            professor = self.session.query(
                professorModel
            ).filter(
                professorModel.identification_card == identification_card
            ).first()
            return professor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()

    def create_professor(self, **kwargs):
        try:
            professor = professorModel(
                fullname=kwargs.get("fullname"),
                identification_card=kwargs.get("identification_card"),
                department=kwargs.get("department"),
                program=kwargs.get("program"),
                highest_education_level=kwargs.get("highest_education_level"),
                degree_obtained=kwargs.get("degree_obtained"),
                undergraduate_degree=kwargs.get("undergraduate_degree"),
                partnership=kwargs.get("partnership"),
                institutional_email=kwargs.get("institutional_email"),
                personal_email=kwargs.get("personal_email"),
                email_with_domain=kwargs.get("email_with_domain"),
                faculty_location=kwargs.get("faculty_location"),
            )
            self.session.add(professor)
            return professor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()

    def update_professor(self, identification_card: int, **kwargs):
        try:
            professor = update(
                professorModel
            ).where(
                professorModel.identification_card == identification_card
            ).values(**kwargs)
            self.session.execute(professor)
            self.session.commit()
            return professor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()
