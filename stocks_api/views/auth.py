from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError
from pyramid.response import Response
from ..models import Account
import json

class AuthAPIViewset(APIViewSet):
    def create(self, request, auth=None):
        """Create a auth instance"""
        data = json.loads(request.body)

        if auth == 'register':
            try:
                user = Account.new(request,
                    data['email'],data['password'],)
            except (IntegrityError, KeyError):
                return Response(json='Bad Request', status=400)

        # TODO: Refactor this to use JSON Web Token
        return Response(json='Created', status=201)

        # if auth == 'login':


        # return Response(json='Not Found', status= 404)


