import graphene

from db_helpers.roleSelection import selectRoleByRoleCode, isRoleByRoleCodeExist

class RoleInput(graphene.InputObjectType):
    roleCode = graphene.String(required=True)
    roleDesc = graphene.String()
    createdBy = graphene.String()
    updatedBy = graphene.String()