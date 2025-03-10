from project.app.professors.entrypoints.requests.createProfesorInput import (
    CreateprofessorSchema
)
from project.app.professors.entrypoints.requests.deleteProfessorInput import (
    DeleteprofessorSchema
)
from project.app.professors.entrypoints.requests.updateProfessorInput import (
    UpdateprofessorSchema
)
from project.app.professors.domain.services.createProfesorService import (
    CreateprofessorService
)
from project.app.professors.domain.services.deleteProfessorService import (
    DeleteprofessorService
)
from project.app.professors.domain.services.updateProfessorService import (
    UpdateprofessorService
)
from project.shared.domain.services.apiResponseService import (
    APIResponseService
)
from project.shared.domain.services.serviceContainer import (
    get_instance
)
from project.shared.domain.utils.apiParamsValidation import (
    ValidationRequestType,
    validate_request
)

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Namespace, Resource
from http import HTTPStatus
from injector import inject
import json

api = Namespace(
    name="professor",
    description="",
    path="/professor"
)

@api.route("/create_professor")
class CreateprofessorView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(CreateprofessorView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=CreateprofessorSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    @jwt_required(locations="query_string")
    def post(self, request):
        try:
            current_user = json.loads(get_jwt_identity())
            service = get_instance(CreateprofessorService)
            output = service.execute(
                role_name=current_user.get("role"),
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

@api.route("/update_professor")
class UpdateprofessorView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(UpdateprofessorView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=UpdateprofessorSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    @jwt_required(locations="query_string")
    def patch(self, request):
        try:
            current_user = json.loads(get_jwt_identity())
            service = get_instance(UpdateprofessorService)
            output = service.execute(
                role_name=current_user.get("role"),
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


@api.route("/delete_professor")
class DeleteprofessorView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(DeleteprofessorView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=DeleteprofessorSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    @jwt_required(locations="query_string")
    def delete(self, request):
        try:
            current_user = json.loads(get_jwt_identity())
            service = get_instance(DeleteprofessorService)
            output = service.execute(
                role_name=current_user.get("role"),
                identification_card=request.get("identification_card")
            )
            return APIResponseService.success(
                output=output,
                status_code=HTTPStatus.OK,
                message="DELETE"
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )
