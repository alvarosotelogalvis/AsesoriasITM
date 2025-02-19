from project.app.schedules.domain.models.schedulesModel import (
    ScheduleModel
)
from project.app.professors.domain.models.professorsModel import (
    professorModel
)
from project.shared.config.database import SessionFactory

from injector import inject
from sqlalchemy import update
from sqlalchemy.orm.exc import FlushError


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

    def get_schedule(self, **kwargs):
        try:
            schedule_querry = self.session.query(ScheduleModel)
            for key, value in kwargs.items():
                schedule_querry = schedule_querry.filter(
                    getattr(ScheduleModel, key) == value
                )
            return schedule_querry.first()
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

    def update_schedule(self, group_id: str, **kwargs):
        try:
            schedule = update(
                ScheduleModel
            ).where(
                ScheduleModel.group_id == group_id
            ).values(**kwargs)
            self.session.execute(schedule)
            self.session.commit()
            return schedule
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()
