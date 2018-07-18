from graphene_sqlalchemy import SQLAlchemyObjectType

# import People Database model
# from people_model import People as PeopleDBModel
from db_models import RoleDBModel
import graphene

# bined with db schema model

class RoleSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = RoleDBModel
        # interfaces = (relay.Node, )


# Base role custom schema class

class Role(graphene.ObjectType):
    rowId = graphene.Int()
    roleCode = graphene.String()
    roleDesc = graphene.String()
    createdAt = graphene.String()
    createdBy = graphene.String()
    updatedAt = graphene.String()
    updatedBy = graphene.String()
