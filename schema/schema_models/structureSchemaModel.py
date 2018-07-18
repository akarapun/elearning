from graphene_sqlalchemy import SQLAlchemyObjectType
from db_models import StructureDBModel

class StructureSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = StructureDBModel

import graphene
from graphene import (
    String,
    Int
)

class Structure(graphene.ObjectType):
    rowId = Int()
    strCode = String()
    strDesc = String()
    createdAt = String()
    createdBy = String()
    updatedAt = String()
    uddatedBy = String()
