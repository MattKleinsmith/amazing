from .models import Product as ProductModel
from .models import User as UserModel

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class Product(SQLAlchemyObjectType):
    class Meta:
        model = ProductModel
        interfaces = (relay.Node,)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)
        exclude_fields = ('hashed_password',)


class Query(graphene.ObjectType):
    # node = relay.Node.Field()
    all_products = SQLAlchemyConnectionField(Product.connection)
    all_users = SQLAlchemyConnectionField(User.connection)


schema = graphene.Schema(query=Query)
