from project.shared.domain.ports.apiResponsePort import (
    APIResponseSuccessPort,
    APIResponseErrorPort,
    APIResponseForbiddenPort,
    APIResponseUnauthenticatedPort
)

from flask import make_response, send_file
from flask_restx import marshal
from datetime import datetime


class APIResponseService(
    APIResponseSuccessPort,
    APIResponseErrorPort,
    APIResponseForbiddenPort,
    APIResponseUnauthenticatedPort
):

    API_VERSION = 'v1'
    
    @staticmethod
    def success(
        output: any,
        model: any = None,
        envelope: str = 'result',
        status_code: int = 200,
        message: str = 'OK',
        version: str = 'v1',
        cookies: dict = None
    ):
        
        structured_output = {'result': output}
        
        if model is not None:
            structured_output = marshal(output, model, envelope=envelope)
        
        response = make_response(
            {
                **structured_output,
                'success': True,
                'message': message,
                'version': version
            },
            status_code
        )

        if cookies is not None:
            for cookie in cookies.items():
                response.set_cookie(
                    *cookie, 
                    httponly=True, 
                    secure=True, 
                    samesite='Strict'
                )

        return response

    @staticmethod
    def error(
        message: str,
        status_code: int = 400,
        version: str = 'v1',
        errors: any = None
    ):
        return make_response(
            {
            'message': message,
            'version': version,
            'errors': errors
            },
            status_code
        )


    @staticmethod
    def forbidden(message: str = 'Forbidden'):
        return APIResponseService.error(message, status_code=403, error_code=403)

    @staticmethod
    def unauthenticated(message: str = 'Unauthenticated'):
        return APIResponseService.error(message, status_code=401, error_code=401)

    @staticmethod
    def send_file(file, download_name: str=None, as_attachment: bool = True):
        if download_name is None:
            download_name = f'File {datetime.now.strftime("%Y%m%d%H%M%S")}'
        return send_file(file, download_name=download_name, as_attachment=as_attachment)
