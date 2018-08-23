from pyramid.response import Response
from pyramid.view import view_config


@view_config(route_name='home', renderer='json', request_method='GET')
def home_view(request):
    """
    This function is responsible for receiving a request, building a response.

     :returns
        A response
    """
    message = 'Hello World'
    return Response(body=message, status=200)


@view_config(route_name='stocks', renderer='json', request_method='GET')
def stocks_view(request):
    """
    This function is responsible for receiving a stocks request, building a stocks response.

     :returns
        A response
    """
    message = 'Stocks!'
    return Response(body=message, status=200)
