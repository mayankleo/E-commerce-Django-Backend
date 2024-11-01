import logging
import pprint

logger = logging.getLogger(__name__)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        # logger.info(f'Request Method: {request.method}')
        # logger.info(f'Request Path: {request.path}')
        # logger.info(f'Request Body: {request.body.decode("utf-8")}')
        
        # headers = dict(request.headers)
        # logger.info('Request Headers:')
        # logger.info(pprint.pformat(headers))

        response = self.get_response(request)

        return response
