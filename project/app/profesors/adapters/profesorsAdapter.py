from project.app.profesors.domain.models.profesors import (
    ProfesorModel
)
from project.shared.config.database import SessionFactory

from sqlalchemy.orm.exc import FlushError
from injector import inject

class ProfesorAdapter:

    @inject
    def __init__(self):
        self.session = SessionFactory

    def get_profesor(self, **kwargs):
        try:
            profesor = self.session.query(
                ProfesorModel
            ).filter(
                ProfesorModel.institutional_email == kwargs.get("institutional_email"),
                ProfesorModel.identification_card == kwargs.get("identification_card")
            ).first()
            return profesor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()

    def get_profesor_by_identification_card(
        self,
        identification_card: int
    ):
        try:
            profesor = self.session.query(
                ProfesorModel
            ).filter(
                ProfesorModel.identification_card == identification_card
            ).first()
            return profesor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()
