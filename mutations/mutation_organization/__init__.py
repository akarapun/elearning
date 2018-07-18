import graphene
from graphene import (
    String,
    Int
)

# Org schema Base class

from schema_models import Org

class OrgCreateInput(graphene.InputObjectType):
    orgCode = String(required=True)
    strCode = String()
    parentOrgCode = String()
    orgTypeCode = String()
    orgDesc = String()
    createdBy = String()
