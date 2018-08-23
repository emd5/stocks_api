from pyramid_restful.routers import ViewSetRouter
from .views.stocks import StocksAPIView
# from .views.auth import AuthAPIView


def includeme(config):
    """Connects the controllers, models, and templates if applicable """
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')
    config.add_route('stocks', 'api/v1/stocks')

    router = ViewSetRouter(config)
    router.register('api/v1/stocks', StocksAPIView, 'stocks')


