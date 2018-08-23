from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def list(self, request):
        """Get a list of all records """
        # http: 6534/api/v1/company/  # <- just an example
        return Response(json={'message': 'Provided a list of companies'}, status=200)

    def create(self, request):
        """Create a records """
        return Response(json={'message': 'Create a new company'}, status=201)

    def retrieve(self, request, id=None):
        """Get one record """
        # http://6543/api/v1/company/{symbol}/

        # Use the 'id' to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(json={'message': 'Provided a single company'}, status=200)

    def destroy(self, request, id=None):
        """Delete a record """
        return Response(json={'message': 'Delete a company'}, status=204)



