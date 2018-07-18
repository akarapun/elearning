from graphene_sqlalchemy import SQLAlchemyObjectType

# import People Database model
# from people_model import People as PeopleDBModel
from db.models import PositionDBModel
import graphene

class PositionSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = PositionDBModel
        # interfaces = (relay.Node, )
