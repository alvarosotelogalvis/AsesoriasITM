from project.app.schedules.domain.config.permittedRoles import (
    permitted_roles_for_schedules
)
from project.app.schedules.domain.ports.schedulesPort import (
    SchedulePort
)

class CreateScheduleService:

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
        # Create schedule
        kwargs.update({"professor_id": professor_id})
        create_schedule = self.schedule_port.create_schedule(**kwargs)
        if not create_schedule:
            raise Exception("The schedule could not be created")
        return {
            "id": create_schedule.id,
            "group_id": create_schedule.group_id,
            "subject": create_schedule.subject,
        }

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
            if get_schedule:
                raise Exception(
                    f"The subject with code '{group_id}' is already assigned to this user.")
        elif role_name == "admin":
            get_schedule = self.schedule_port.get_schedule(
                **{
                    "group_id": group_id,
                    "deleted_at": None
                }
            )
            if get_schedule:
                raise Exception(
                    f"The subject with code '{group_id}' is create.")
