from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from pyramid.view import view_config
from ..models.schemas import StockSchema
from ..models.stock import Stock
from ..models.account import Account

import json
import requests

API_URL = 'https://api.iextrading.com/1.0/'


@view_config(route_name='lookup', renderer='json', request_method='GET')
def lookup(request):
    """ Grabs id
    :param request:
    :return:
    """
    symbol = request.matchdict['symbol']
    url = f'{API_URL}stock/{symbol}/company'
    response = requests.get(url)

    return Response(json=response.json(), status=200)


class StockAPIViewset(APIViewSet):
    """ Must validate here!! The gatekeeper"""

    def create(self, request):
        """ Create one new stock"""
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'symbol' not in kwargs:
            return Response(json='Expected value: symbol', status=400)

        #  Authentication required for managing model relationships
        if request.authenticated_userid:
            account = Account.one(request, request.authenticated_userid)
            kwargs['account.id'] = account.id

        try:
            stock = Stock.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Stocks already exists', status=409)

        schema = StockSchema()  # From marshmallows serializer class
        data = schema.dump(stock).data  # Representation of JSON data, property of the marshmallow instance
        return Response(json=data, status=201)

    def list(self, request):
        """Get all stocks """
        # Serialized everything in the list
        records = Stock.all(request)
        schema = StockSchema()
        data = [schema.dump(record).data for record in records]

        return Response(json=data, status=200)

    def retrieve(self, request, id=None):
        """ Get one stock """
        record = Stock.one(request, id)
        if not record:
            return Response(json='Record not Found', status=404)

        schema = StockSchema()
        data = schema.dump(record).data

        return Response(json=data, status=200)

    def destroy(self, request, id=None):
        """ Delete a stock"""
        if not id:
            return Response(json='Not found', status=404)

        try:
            Stock.remove(request=request, pk=id)
        except (DataError, AttributeError):
            return Response(json="Not Found", status=404)

        return Response(status=204)

