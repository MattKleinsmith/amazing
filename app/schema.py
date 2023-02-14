from .models import Product as ProductModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    all_products = SQLAlchemyConnectionField(Product.connection)


schema = graphene.Schema(query=Query)
