from pyramid_restful.routers import ViewSetRouter
from .views.company import CompanyAPIViewset
from .views.location import StockAPIViewset


def includeme(config):
    """Connects the controllers, models, and templates if applicable """
    config.add_static_view('static', 'static', cache_max_age=3600)

    config.add_route('home', '/')  # binds route name to path
    config.add_route('lookup', '/api/v1/lookup/{zip_code}')

    router = ViewSetRouter(config)
    router.register('api/v1/company', CompanyAPIViewset, 'company')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
    router.register('api/v1/portfolio', StockAPIViewset, 'portfolio')



