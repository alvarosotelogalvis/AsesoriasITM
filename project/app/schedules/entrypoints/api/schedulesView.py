from project.app.schedules.domain.services.createScheduleService import (
    CreateScheduleService
)
from project.app.schedules.domain.services.getAllScheduleService import (
    GetAllScheduleService
)
from project.app.schedules.domain.services.updateScheduleService import (
    UpdateScheduleService
)
from project.app.schedules.entrypoints.requests.createScheduleInput import (
    CreateScheduleSchema
)
from project.app.schedules.entrypoints.requests.getAllScheduleInput import (
    GetAllScheduleSchema
)
from project.app.schedules.entrypoints.requests.updateScheduleInput import (
    UpdateScheduleSchema
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

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource
from http import HTTPStatus
from injector import inject
import json

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


@api.route("/create_schedule")
class CreateScheduleView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(CreateScheduleView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=CreateScheduleSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    @jwt_required(locations="query_string")
    def post(self, request):
        try:
            current_user = json.loads(get_jwt_identity())
            service = get_instance(CreateScheduleService)
            output = service.execute(
                role_name=current_user.get("role"),
                professor_id=current_user.get("id"),
                **request
            )
            return APIResponseService.success(
                output=output,
                status_code=HTTPStatus.CREATED,
                message="CREATED"
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )

@api.route("/update_schedule")
class UpdateScheduleView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(UpdateScheduleView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=UpdateScheduleSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    @jwt_required(locations="query_string")
    def patch(self, request):
        try:
            current_user = json.loads(get_jwt_identity())
            service = get_instance(UpdateScheduleService)
            output = service.execute(
                role_name=current_user.get("role"),
                professor_id=current_user.get("id"),
                **request
            )
            return APIResponseService.success(
                output=output,
                status_code=HTTPStatus.CREATED,
                message="UPDATED"
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )
