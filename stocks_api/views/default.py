from pyramid.response import Response  # generates a response from the pyramid library
from pyramid.view import view_config


@view_config(route_name='home',renderer='json',request_method='GET')
def home_view(request):
    """
    This function is responsible for receiving a request, building a response.

     :returns
        A json response 'Hello World'
    """
    message = '''
        GET / - Base API route\n
        POST /api/v1/auth/ - Register a new account\n
        GET /api/v1/auth/ - Login to an existing account\n
        GET /api/v1/stocks/ - Retrieve all stock information\n
        GET /api/v1/stocks/<int>/ - Retrieve specific stock record\n
        POST /api/v1/stocks/ - Create new stock record\n
        DELETE /api/v1/stocks/<int>/ - Remove existing stock record\n
    '''
    return Response(body=message, content_type='text/plain', status=200)


