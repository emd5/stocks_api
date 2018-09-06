import pytest
import requests
from pyramid import testing
from ..models.meta import Base
from ..models.account import Account



@pytest.fixture(scope='session')
def load_db_roles(session):
    """Create roles in the db."""
    from ..models import AccountRole
    roles = ['admin', 'view']
    for role in roles:
        model = AccountRole(name=role)
        requests.dbsession.add(model)


# @pytest.fixture
# def configuration(request):
#     """Setup a database for testing purposes."""
#     config = testing.setUp(settings={
#         'sqlalchemy.url': 'postgres://localhost:5432/stocks_test'
#         # 'sqlalchemy.url': os.environ['TEST_DATABASE_URL']
#     })
#     config.include('stocks_api.models')
#     config.include('stocks_api.routes')
#
#     def teardown():
#         testing.tearDown()
#
#     request.addfinalizer(teardown)
#     return config
#
#
# @pytest.fixture
# def db_session(configuration, request):
#     """Create a database session for interacting with the test database."""
#     SessionFactory = configuration.registry['dbsession_factory']
#     session = SessionFactory()
#     engine = session.bind
#     Base.metadata.create_all(engine)
#
#     def teardown():
#         session.transaction.rollback()
#         Base.metadata.drop_all(engine)
#
#     request.addfinalizer(teardown)
#     return session
#
#
# @pytest.fixture
# def dummy_request(db_session):
#     """Create a dummy GET request with a dbsession."""
#     return testing.DummyRequest(dbsession=db_session)
#
#
# @pytest.fixture
# def test_user():
#     """Set up a test user"""
#     return Account(
#         username="testtest",
#         password="testpass",
#         email="test@testthis.com",
#         admin=True,
#     )
#
#
# @pytest.fixture
# def add_user(dummy_request, test_user):
#     """Add a user to database"""
#     dummy_request.dbsession.add(test_user)
#     return test_user
