
class APIResponseSuccessPort:
    @staticmethod
    def success(
        output: any,
        model: any,
        status_code: int,
        message: str,
        version: str,
        cookies: dict = None
    ):
        raise NotImplementedError
    

class APIResponseErrorPort:
    @staticmethod
    def error(
        message: str,
        status_code: int,
        version: str,
        errors: any = None
    ):
        raise NotImplementedError
    

class APIResponseForbiddenPort:
    @staticmethod
    def forbidden(
        message: str
    ):
        raise NotImplementedError
    
class APIResponseUnauthenticatedPort:
    @staticmethod
    def unauthenticated(
        message: str
    ):
        raise NotImplementedError
