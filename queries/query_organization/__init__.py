import graphene
from graphene import (
    String,
    Int
)

# Base

from schema_models import Org

class Organization(graphene.ObjectType):
    orgCode = String()
