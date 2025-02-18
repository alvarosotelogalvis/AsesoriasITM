from project.app.schedules.domain.ports.schedulesPort import (
    SchedulePort
)
from project.shared.domain.services.paginatorService import (
    PaginatorService
)

class GetAllScheduleService:

    def __init__(
        self,
        schedule_port: SchedulePort,
        paginator_service: PaginatorService,
    ):
        self.schedule_port = schedule_port
        self.paginator_service = paginator_service

    def execute(
        self,
        page: int = 1,
        per_page: int = 10
    ):
        schedules_query = self.schedule_port.get_all_schedules()
        paginator = self.paginator_service.paginate_base_query(
            query=schedules_query,
            page=page,
            per_page=per_page
        )
        return paginator
