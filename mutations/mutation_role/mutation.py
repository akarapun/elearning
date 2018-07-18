import graphene

from mutation_role.createRole import CreateRoleMutation
from mutation_role.updateRole import UpdateRoleMutation
from mutation_role.deleteRole import DeleteRoleMutation

class RoleMutation(
    CreateRoleMutation,
    UpdateRoleMutation,
    DeleteRoleMutation,
    graphene.ObjectType):
    pass
