from graphene_sqlalchemy import SQLAlchemyObjectType

# import People Database model
# from people_model import People as PeopleDBModel
from db_models.PeopleCredential import PeopleCredential as PeopleCredentialDBModel
import graphene

class PeopleCredential(SQLAlchemyObjectType):
    class Meta():
        model = PeopleCredentialDBModel
        # interfaces = (relay.Node, )
