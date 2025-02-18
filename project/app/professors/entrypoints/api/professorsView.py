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
    name="Profesor",
    description="",
    path="/profesor"
)

@api.route("/create_profesor")
class CreateProfesorView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(CreateProfesorView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=SignUpSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    def post(self, request):
        pass