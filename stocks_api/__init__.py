from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application. Entry point of the application
    """
    config = Configurator(settings=settings)
    config.include('pyramid_restful')
    # config.include('.models')
    config.include('.routes') #relative path to

    config.scan() # looks at @view_config
    return config.make_wsgi_app() #this is http server web server gateway interface
