from pyramid.response import Response  # generates a response from the pyramid library
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """
    This function is responsible for receiving a request, building a response.

     :returns
        A json response 'Hello World'
    """
    message = '''
    Hello World
    '''
    return Response(body=message, content_type='text/plain', status=200)


