import graphene
from graphene import (
    String,
    Int
)
from graphene_sqlalchemy import SQLAlchemyObjectType
from db_models import OrganizationDBModel

class OrganizationSchemaModel(SQLAlchemyObjectType):
    class Meta():
        model = OrganizationDBModel

class Org(graphene.ObjectType):
    orgCode = String()
    strCode = String()
    parentOrgCode = String()
    orgTypeCode = String()
    orgDesc = String()
    createdAt = String()
    createdBy = String()
    updatedAt = String()
    updatedBy = String()
