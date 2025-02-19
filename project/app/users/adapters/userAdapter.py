from project.app.users.domain.models.userModel import UserModel
from project.shared.config.database import SessionFactory

from datetime import datetime
from injector import inject
from sqlalchemy.orm.exc import FlushError

class UserAdapter:

    @inject
    def __init__(self):
        self.session = SessionFactory

    def get_user_by_username(self, username: str):
        try:
            get_login = self.session.query(
                UserModel
            ).filter(
                UserModel.username == username,
                UserModel.deleted_at.is_(None)
            ).first()
            return get_login
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.close()

    def create_user(self, **kwargs):
        try:
            user = UserModel(
                username=kwargs.get("institutional_email"),
                professor_id=kwargs.get("professor_id")
            )
            user.set_password(kwargs.get("password"))
            self.session.add(user)
            return user
        except FlushError as error:
            self.session.rollback()
            raise Exception(error)
        except Exception as error:
            self.session.rollback()
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()

    def delete_user(self, professor_id: str):
        try:
            professor = self.session.query(
                UserModel
            ).filter(
                UserModel.professor_id == professor_id
            ).update(
                {UserModel.deleted_at: datetime.now()}
            )
            return professor
        except FlushError as error:
            raise Exception(error)
        except Exception as error:
            raise Exception(error)
        finally:
            self.session.commit()
            self.session.close()
