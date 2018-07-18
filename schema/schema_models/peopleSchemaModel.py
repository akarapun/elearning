from graphene_sqlalchemy import SQLAlchemyObjectType

from db_models import PeopleDBModel
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

class PeopleSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = PeopleDBModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_peoples = SQLAlchemyConnectionField(PeopleSchemaModel)
    
schema = graphene.Schema(query=Query)

     
