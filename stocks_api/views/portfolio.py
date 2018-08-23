from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class PortfolioAPIViewset(APIViewSet):
    def list(self, request):
        """Get all portfolios """
        return Response(json={'message': 'Provided a list of portfolio'}, status=200)

    def create(self, request):
        """Create a new portfolio """
        return Response(json={'message': 'Create a new portfolio'}, status=201)

    def retrieve(self, request, id=None):
        """Get one portfolio """
        return Response(json={'message': 'Get one portfolio'}, status=200)

    def destroy(self, request, id=None):
        """Delete a portfolio """
        return Response(json={'message': 'Delete a stock'}, status=204)
