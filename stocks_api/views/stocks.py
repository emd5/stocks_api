from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StockAPIViewset(APIViewSet):
    def list(self, request):
        """Get all records """
        return Response(json={'message': 'Provided a list of stocks'}, status=200)

    def create(self, request):
        """ Create one new stock"""
        return Response(json={'message': 'Create a new stock'}, status=201)

    def retrieve(self, request, id=None):
        """ Get a stock """
        return Response(json={'message': 'Get a stock'}, status=200)

    def destroy(self, request, id=None):
        """ Delete a stock"""
        return Response(json={'message': 'Delete a stock'}, status=204)

