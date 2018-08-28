from marshmallow_sqlalchemy import ModelSchema
from . import Portfolio
from . import Stock
from . import Company


class StockSchema(ModelSchema):
    class Meta:
        model = Stock


class PortfolioSchema(ModelSchema):
    class Meta:
        model = Portfolio


class CompanySchema(ModelSchema):
    class Meta:
        model = Company
