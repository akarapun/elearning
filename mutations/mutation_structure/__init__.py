import graphene
from graphene import (
    String,
    Int
)

from schema_models import Structure

class CreateStructureInput(graphene.InputObjectType):
    strCode = String(required=True)
    strDesc = String()
    createdBy = String(required=True)


class UpdateStructureInput(graphene.InputObjectType):
    strCode = String(required=True)
    strDesc = String()
    updatedBy = String(required=True)
