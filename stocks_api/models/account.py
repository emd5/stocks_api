from .portfolio import Portfolio
from sqlalchemy.orm import relationship
from .role import AccountRole
from .associations import roles_association
from sqlalchemy.exc import DBAPIError
from .meta import Base
from datetime import datetime as dt
from cryptacular import bcrypt  #  blackbox: hash and check pw
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime,
)

manager = bcrypt.BCRYPTPasswordManager()


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
        self.password = manager.encode(password, 10)  # NOTE: 10 indicates a level of complexity

    @classmethod
    def new(cls, request, email=None, password=None):
        """Register a new user"""
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)  # generate user add to db

        # NOT SAve
        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none()

        user.roles.append(admin_role)

        # I made a change and i need to commit that trans before return out
        # of function, if not flush the admin wont save
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def one(cls,request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        """Validate that user exist and they are who they say they are"""

        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(
                cls.email == email).one_or_none()

        except DBAPIError:
            return None

        if account is not None:
            if manager.check(account.password, password):
                return account

        return None


