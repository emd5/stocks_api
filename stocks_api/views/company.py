from sqlalchemy.exc import IntegrityError, DataError
from pyramid_restful.viewsets import APIViewSet
from pyramid.response import Response
from ..models.schemas import CompanySchema
from ..models.company import Company
import json


class CompanyAPIViewset(APIViewSet):
    def create(self, request):
        """ Create one new company"""
        try:
            kwargs = json.loads(request.body)
        except json.JSONDecodeError as e:
            return Response(json=e.msg, status=400)

        if 'id' not in kwargs:
            return Response(json='Expected value: company', status=400)

        try:
            company= Company.new(request, **kwargs)
        except IntegrityError:
            return Response(json='Duplicate Key Error. Company already exists', status=409)

        schema = CompanySchema()  # From marshmallows serializer class
        data = schema.dump(company).data  # Representation of JSON data, property of the marshmallow instance
        return Response(json=data, status=201)

    def list(self, request):
        """Get a list of all companies """
        # http: 6534/api/v1/company/  # <- just an example
        return Response(json={'message': 'Provided a list of companies'}, status=200)

    def retrieve(self, request, id=None):
        """Get one company """
        # http://6543/api/v1/company/{symbol}/

        # Use the 'id' to lookup that resource in the DB,
        # Formulate a response and send it back to the client
        return Response(json={'message': 'Provided a single company'}, status=200)

    def destroy(self, request, id=None):
        """Delete a company """
        return Response(json={'message': 'Delete a company'}, status=204)



