from project.app.schedules.domain.models.schedulesModel import (
    ScheduleModel
)
from project.app.professors.domain.models.professorsModel import (
    professorModel
)
from project.shared.config.database import SessionFactory

from sqlalchemy.orm.exc import FlushError
from injector import inject


class ScheduleAdapter:

    @inject
    def __init__(self):
        self.session = SessionFactory

    def get_all_schedules(self):
        try:
            query = self.session.query(
                professorModel.fullname,
                professorModel.institutional_email,
                ScheduleModel.group_id,
                ScheduleModel.subject,
                ScheduleModel.schedule,
                ScheduleModel.classroom,
            ).join(
                professorModel
            )
            # schedules = self.session.execute(query).mappings().all()
            return query
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()
