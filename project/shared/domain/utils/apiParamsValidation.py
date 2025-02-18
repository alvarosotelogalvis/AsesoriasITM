from enum import Enum
from flask import request, jsonify, make_response
from functools import wraps


class ValidationRequestType(Enum):
    QUERY_PARAMS = "QUERY_PARAMS"
    ROUTE_PARAMS = "ROUTE_PARAMS"
    BODY_PARAMS = "BODY_PARAMS"


def validate_request(schema, with_types: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            params = {}
            for type in with_types:
                if type == ValidationRequestType.ROUTE_PARAMS:
                    params.update(**kwargs)
                
                if type == ValidationRequestType.QUERY_PARAMS:
                    params.update(**request.args.to_dict())
                                        
                if type == ValidationRequestType.BODY_PARAMS:
                    params.update(**request.get_json())
            
            
            errors = schema().validate(params)
            if errors:
                return make_response(jsonify({"errors": errors}), 400)
            return func(*args, **kwargs, request=params)
        return wrapper
    return decorator