from project.app.schedules.domain.services.getAllScheduleService import (
    GetAllScheduleService
)
from project.app.schedules.entrypoints.requests.getAllScheduleInput import (
    GetAllScheduleSchema
)
from project.shared.domain.services.apiResponseService import (
    APIResponseService
)
from project.shared.domain.utils.apiParamsValidation import (
    ValidationRequestType,
    validate_request
)
from project.shared.domain.services.serviceContainer import (
    get_instance
)

from flask_restx import Namespace, Resource
from http import HTTPStatus
from injector import inject

api = Namespace(
    name="Schedules",
    description="",
    path="/schedules"
)

@api.route("/get_all_schedule")
class GetAllScheduleView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(GetAllScheduleView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=GetAllScheduleSchema,
        with_types=[ValidationRequestType.QUERY_PARAMS]
    )
    def get(self, request):
        try:
            service = get_instance(GetAllScheduleService)
            output = service.execute(
                page=int(request.get("page")),
                per_page=int(request.get("per_page"))
            )
            return APIResponseService.success(
                output=output
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )
