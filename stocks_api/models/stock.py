from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)


from .meta import Base


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    company_name = Column(Text, unique=True, nullable=False)
    exchange = Column(Integer, unique=True, nullable=False)
    industry = Column(Integer, unique=True, nullable=False)
    website = Column(Integer, unique=True, nullable=False)
    description = Column(Integer, unique=True, nullable=False)
    ceo = Column(Integer, unique=True, nullable=False)
    issue_type = Column(Integer, unique=True, nullable=False)
    sector = Column(Integer, unique=True, nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    @classmethod
    def one(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError
        return request.dbsession.query(cls).get(pk)

    @classmethod
    def new(cls, request, **kwargs):
        if request.dbsession is None:
            raise DBAPIError

        # stock = StocksLocation({'name': 'some name', 'zip_code': 98038})
        stock = cls(**kwargs)
        request.dbsession.add(stock)

        return request.dbsession.query(cls).filter(
            cls.zip_code == kwargs['zip_code']).one_or_none()  # returns a query object one or none

    @classmethod
    def destroy(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(cls.id == pk).delete()

    @classmethod
    def all(cls, request):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()





