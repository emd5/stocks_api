from sqlalchemy import Table, Column, Integer, ForeignKey
from .meta import metadata


#  This file representation is the db association (junction) for the accounts and roles db
# This file represents a many to many relationship between accounts and account roles
roles_association = Table(
    'roles_association',
    metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id')),
)

#  Alternate method of writing the above
#  from .meta import Base
# class RolesAssociation(Base):
#     __tablename__ = 'roles_association'
#     account_id = Column(Integer, ForeignKey('accounts.id'))
#     role_id = Column(Integer, ForeignKey('account_roles.id'))
