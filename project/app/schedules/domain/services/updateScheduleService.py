from project.app.schedules.domain.config.permittedRoles import (
    permitted_roles_for_schedules
)
from project.app.schedules.domain.ports.schedulesPort import (
    SchedulePort
)

class UpdateScheduleService:

    def __init__(
        self,
        schedule_port: SchedulePort
    ):
        self.schedule_port = schedule_port

    def execute(self, role_name: str, professor_id: int, **kwargs):
        # Validations
        self.__validate_role(role_name=role_name)
        self.__validate_group(
            role_name=role_name,
            group_id=kwargs.get("group_id"),
            professor_id=professor_id
        )
        # Update schedule
        self.schedule_port.update_schedule(
            **kwargs
        )
        return {"successful": "The schedule was updated correctly"}

    def __validate_role(self, role_name: str):
        if role_name not in permitted_roles_for_schedules:
            raise Exception(
                "The user does not have permissions to perform this action.")
    
    def __validate_group(self, role_name: str, group_id: str, professor_id: int):
        if role_name == "professor":
            get_schedule = self.schedule_port.get_schedule(
                **{
                    "group_id": group_id,
                    "professor_id": professor_id,
                    "deleted_at": None
                }
            )
            if not get_schedule:
                raise Exception(
                    f"the subject does not exist or does not belong to the user.")
        elif role_name == "admin":
            get_schedule = self.schedule_port.get_schedule(
                **{
                    "group_id": group_id,
                    "deleted_at": None
                }
            )
            if not get_schedule:
                raise Exception(
                    f"the subject does not exist.")
