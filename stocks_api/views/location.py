from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
from ..models.schemas import StockSchema
from ..models.stock import Stock
import json
import requests


#  vanilla pyramid syntax, hacky way
@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """
    Grabs zip code
    :param request:
    :return:
    """
    url = 'https://api.openstocksmap.org/....'.format(request.matchdict['zip_code'])
    response = requests.get(url)
    return response(json='response.json', status=200)


class StockAPIViewset(APIViewSet):
    def create(self, request):
        """ Create one new stock"""
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'zip_code' not in kwargs:
            return Response(json='Expected value: stocks', status=400)

        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stocks already exists', status=409)

        schema = StockSchema()  # From marshmallows serializer class
        data = schema.dump(stock).data  # Representation of JSON data, property of the marshmallow instance
        return Response(json=data, status=201)

    def list(self, request):
        """Get all records """
        return Response(json={'message': 'Provided a list of stocks'}, status=200)

    def retrieve(self, request, id=None):
        """ Get a stock """
        return Response(json={'message': 'Get a stock'}, status=200)

    def destroy(self, request, id=None):
        """ Delete a stock"""
        if not id:
            return Response(json='Not found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json="Not Found", status=404)

        return Response(status=204)
