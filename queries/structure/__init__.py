import graphene

from schema_models import Structure

class IndividualStructure(
    Structure,
    graphene.ObjectType): pass
