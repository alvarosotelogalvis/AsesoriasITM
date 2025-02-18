from project.app.professors.entrypoints.requests.createProfesorInput import (
    CreateprofessorSchema
)
from project.app.professors.domain.services.createProfesorService import (
    CreateprofessorService
)
from project.shared.domain.services.serviceContainer import (
    get_instance
)
from project.shared.domain.utils.apiParamsValidation import (
    ValidationRequestType,
    validate_request
)

from flask_restx import Namespace, Resource
from http import HTTPStatus
from injector import inject

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
    def post(self, request):
        service = get_instance(CreateprofessorService)
        output = service.execute(**request)
