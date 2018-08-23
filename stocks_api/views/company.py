from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response


class CompanyAPIViewset(APIViewSet):
    def retrieve(self, request, id):
        # http://6543/api/v1/company/{symbol}/

        # Use the 'id' to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(
            json={f'message': 'Provided a single resource for {id}'},
            status=200
        )

    # def list(self, request):
    #     # http: 6534/api/v1/company/  # <- just an example
    #     pass

    def create(self, request):
        pass

    def destroy(self, request):
        pass


