import graphene

from mutation_structure.createStructure import CreateStructureMutation
from mutation_structure.updateStructure import UpdateStructureMutation
from mutation_structure.deleteStructure import DeleteStructureMutation

class StructureMutation(
    CreateStructureMutation,
    UpdateStructureMutation,
    DeleteStructureMutation,
    graphene.ObjectType):
    pass
