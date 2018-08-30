from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock, Company, Account, AccountRole


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class CompanySchema(ModelSchema):
    class Meta:
        model = Company


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    # all marshmallow - go get the records that belong to the id
    # This is really just an example of multiple fields
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    class Meta:
        model = Account


class StockSchema(ModelSchema):
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema,
    exclude=('password', 'locations', 'roles', 'date_created', 'date_updated'
             ))
    class Meta:
        model = Stock



