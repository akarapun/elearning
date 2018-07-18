import graphene
from schema_models import Structure
from db_helpers.structureSelection import selectAllStructure

class GetAllStructure(graphene.ObjectType):
    structure = graphene.List(Structure)

    def resolve_structure(self, info):

        import utils
        if utils.isAllowAccess():
            return selectAllStructure()
