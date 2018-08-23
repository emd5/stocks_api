from pyramid_restful.routers import ViewSetRouter
from .views import CompanyAPIViewset, StockAPIViewset


def includeme(config):
    """Connects the controllers, models, and templates if applicable """
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')  # binds route name to path

    router = ViewSetRouter(config)
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')


