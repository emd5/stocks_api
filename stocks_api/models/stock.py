from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import(
    Column,
    Index,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)


from .meta import Base


class Stock(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    company_name = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Integer)
    description = Column(Text)
    ceo = Column(Text)
    issue_type = Column(Text)
    sector = Column(Text)

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
            cls.symbol == kwargs['symbol']).one_or_none()  # returns a query object one or none

    @classmethod
    def remove(cls, request=None, pk=None):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(cls.id == pk).delete()

    @classmethod
    def all(cls, request):
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()





