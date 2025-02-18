from project.app.users.domain.services.signUpService import (
    SignUpService
)
from project.app.users.domain.services.signInService import (
    SignInService
)
from project.app.users.entrypoints.requests.signUpInput import (
    SignUpSchema
)
from project.app.users.entrypoints.requests.signInInput import (
    SignInSchema
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

from flask_restx import Namespace, Resource
from http import HTTPStatus
from injector import inject

api = Namespace(
    name="Login",
    description="",
    path="/login"
)

@api.route("/sign_up")
class SignUpView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(SignUpView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=SignUpSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    def post(self, request):
        try:
            service = get_instance(SignUpService)
            return service.execute(
                institutional_email=request.get("institutional_email"),
                identification_card=request.get("identification_card"),
                password=request.get("password")
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )


@api.route("/sign_in")
class SignInView(Resource):
    
    @inject
    def __init__(self, api=None, *args, **kwargs):
        super(SignInView, self).__init__(api, *args, **kwargs)
        self.get_instance = get_instance
        # self.log = logging.getLogger('application.api')

    @validate_request(
        schema=SignInSchema,
        with_types=[ValidationRequestType.BODY_PARAMS]
    )
    def post(self, request):
        try:
            service = get_instance(SignInService)
            return service.execute(
                username=request.get("username"),
                password=request.get("password")
            )
        except Exception as error:
            return APIResponseService.error(
                message=str(error)
            )
