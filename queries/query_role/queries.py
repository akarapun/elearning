import graphene

from query_role.getAllRole import GetAllRole
from query_role.roleByRoleCode import RoleByRoleCode

class RoleQueries(
    GetAllRole,
    RoleByRoleCode,
    graphene.ObjectType):
    pass
