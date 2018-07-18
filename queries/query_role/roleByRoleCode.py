import graphene

import schema_models

class RoleByRoleCodeResult(graphene.ObjectType):
    role = graphene.Field(schema_models.Role)
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

class RoleByRoleCode(graphene.ObjectType):
    roleByRoleCode = graphene.Field(RoleByRoleCodeResult, roleCode=graphene.String())

    def resolve_roleByRoleCode(self, info, roleCode):

        import utils
        if utils.isAllowAccess():

            result = RoleByRoleCodeResult()

            from db_helpers.roleSelection import selectRoleByRoleCode
            role = selectRoleByRoleCode(roleCode, info)

            if role is not None:
                result.role = role
                result.status = True
            else:
                result.msg = 'This PosCode: \'{}\' is not exist.'.format(roleCode)

            return result
