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

    def get_schedules_by_group(self, group_id: int, professor_id: int):
        try:
            schedule = self.session.query(
                ScheduleModel
            ).filter(
                ScheduleModel.group_id == group_id,
                ScheduleModel.professor_id == professor_id,
                ScheduleModel.deleted_at.is_(None)
            ).first()
            return schedule
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()
    
    def create_schedule(self, **kwargs):
        try:
            schedule = ScheduleModel(
                group_id=kwargs.get("group_id"),
                subject=kwargs.get("subject"),
                schedule=kwargs.get("schedule"),
                classroom=kwargs.get("classroom"),
                academic_program=kwargs.get("academic_program"),
                professor_id=kwargs.get("professor_id")
            )
            self.session.add(schedule)
            return schedule
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()
