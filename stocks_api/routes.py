from pyramid_restful.routers import ViewSetRouter
from .views.company import CompanyAPIViewset
from .views.stock import StockAPIViewset
from .views.auth import AuthAPIViewset
from .views.portfolio import PortfolioAPIViewset
from .views.visuals import VisualAPIViewset


def includeme(config):
    """Connects the controllers, models, and templates if applicable """
    config.add_static_view('static', 'static', cache_max_age=3600) # for nginx, to distribute

    # Vanilla pyramid, using base name (routename on view config decorator) binds route name to path
    config.add_route('home', '/')
    config.add_route('lookup', '/api/v1/lookup/{symbol}')

    # This is pyramid restful framework
    router = ViewSetRouter(config, trailing_slash=False)
    # Reference the link with aliases
    router.register('api/v1/company', CompanyAPIViewset, 'company', permission='admin')
    router.register('api/v1/stocks', StockAPIViewset, 'stocks')
    router.register('api/v1/auth/{auth}', AuthAPIViewset, 'auth')
    router.register('api/v1/portfolio', PortfolioAPIViewset, 'portfolio')
    router.register('api/v1/visuals', VisualAPIViewset, 'visuals')


