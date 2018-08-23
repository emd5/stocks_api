from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class StockAPIViewset(APIViewSet):
    def list(self, request):
        """Get all records"""
        return Response(json={'message': 'Provide a list of stocks'}, status=200)

    def create(self, request):
        return Response(json={'message': f'Create a new resource for {id}'}, status=200)

    def retrieve(self, request):
        return Response(json={'message': 'Created a new record'}, status=201)

    def destroy(self, request, id):
        return Response(json={'message': 'Delete the record'}, status=204)

