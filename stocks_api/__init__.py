from pyramid.config import Configurator
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.security import Allow, ALL_PERMISSIONS


class RootACL:
    __acl__ = [
        (Allow, 'admin', ALL_PERMISSIONS),
        (Allow, 'view', ['read']),
    ]

    def __init__(self, request):
        pass


def add_role_principals(userid, request):
    return request.jwt_claims.get('roles', [])


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. Entry point of the application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jwt')
    config.include('pyramid_restful')

    config.set_root_factory(RootACL)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    config.set_jwt_authentication_policy(
        'superseekretseekrit',  # os.environ.get('SECRET', None)
        auth_type='Bearer',
        callback=add_role_principals,
    )

    config.include('.models')
    config.include('.routes')  # points to routes.py looks at includeme()

    config.scan()  # looks at @view_config decorator, tells app to look at them, gather them and use them as controllers
    return config.make_wsgi_app()  # this is http server web server gateway interface, server that booting it keeping it running
