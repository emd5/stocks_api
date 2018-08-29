from .portfolio import Portfolio
from sqlalchemy.orm import relationship
from .role import AccountRole
from .associations import roles_association
from sqlalchemy.exc import DBAPIError
from .meta import Base
from datetime import datetime as dt
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    portfolio = relationship(Portfolio, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')
    date_created = Column(DateTime, default=dt.now())
    date_update = Column(DateTime, default=dt.now(), onupdate=dt.now())

    def __init__(self, email, password=None):
        self.email = email
        self.password = password  # NOTE: THIS IS UNSAFE ND WILL BE FIXED

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user"""
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)  # generate user add to db

        # TODO: assign roles to new user

        return request.dbsession.query(cls).filter(cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that user exist and they are who they say they are"""
        # TODO: Complete this tomorrow as part of the login process
        pass

