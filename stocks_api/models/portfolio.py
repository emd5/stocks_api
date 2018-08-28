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


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
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
        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)

        return request.dbsession.query(cls).filter(
            cls.id == kwargs['id']).one_or_none()  # returns a query object one or none

    # @classmethod
    # def all(cls, request):
    #     if request.dbsession is None:
    #         raise DBAPIError
    #
    #     return request.dbsession.query(cls).all()
    #
    # @classmethod
    # def remove(cls, request=None, pk=None):
    #     if request.dbsession is None:
    #         raise DBAPIError
    #
    #     return request.dbsession.query(cls).filter(cls.id == pk).delete()


