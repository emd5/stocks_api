from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.response import Response
from pyramid.view import view_config
from ..models.schemas import StockSchema
from ..models.stock import Stock
import json
import requests


# #  vanilla pyramid syntax, hacky way
# @view_config(route_name='lookup', renderer='json', request_method='GET')
# def lookup(request):
#     """Grabs zip code
#     :param request:
#     :return:
#     """
#     url = 'https://api.iextrading.com/1.0'.format(request.matchdict['id'])
#     response = requests.get(url)
#     return response(json='response.json', status=200)


class StockAPIViewset(APIViewSet):
    def create(self, request):
        """ Create one new stock"""
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'id' not in kwargs:
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


# class PortfolioAPIViewset(APIViewSet):
#     def list(self, request):
#         """Get all portfolios """
#         return Response(json={'message': 'Provided a list of portfolios'}, status=200)
#
#     def create(self, request):
#         """Create a new portfolio """
#         return Response(json={'message': 'Create a new portfolio'}, status=201)
#
#     def retrieve(self, request, id=None):
#         """Get one portfolio """
#         return Response(json={'message': 'Get one portfolio'}, status=200)
#
#     def destroy(self, request, id=None):
#         """Delete a portfolio """
#         return Response(json={'message': 'Delete a stock'}, status=204)
#
#
# class CompanyAPIViewset(APIViewSet):
#     def list(self, request):
#         """Get a list of all records """
#         # http: 6534/api/v1/company/  # <- just an example
#         return Response(json={'message': 'Provided a list of companies'}, status=200)
#
#     def create(self, request):
#         """Create a records """
#         return Response(json={'message': 'Create a new company'}, status=201)
#
#     def retrieve(self, request, id=None):
#         """Get one record """
#         # http://6543/api/v1/company/{symbol}/
#
#         # Use the 'id' to lookup that resource in the DB,
#         # Formulate a response and send it back to the client
#         return Response(json={'message': 'Provided a single company'}, status=200)
#
#     def destroy(self, request, id=None):
#         """Delete a record """
#         return Response(json={'message': 'Delete a company'}, status=204)
