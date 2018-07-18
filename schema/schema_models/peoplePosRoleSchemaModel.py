import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from db_models import PeoplePosRoleDBModel

class PeoplePosRoleSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = PeoplePosRoleDBModel
