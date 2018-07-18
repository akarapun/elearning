import graphene

from queries.structure.all import GetAllStructure
from queries.structure.structureByStrCode import GetStructureByStrCode

class StructureQueries(
    GetAllStructure,
    GetStructureByStrCode,
    graphene.ObjectType): pass
