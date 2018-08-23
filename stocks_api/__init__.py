from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. Entry point of the application
    """
    config = Configurator(settings=settings)
    config.include('pyramid_restful')
    # config.include('.models') # don't pay attention to this folder
    config.include('.routes') # points to routes.py looks at includeme()

    config.scan()  # looks at @view_config decorator, tells app to look at them, gather them and use them as controllers
    return config.make_wsgi_app()  # this is http server web server gateway interface
