import graphene

from db import db_session
from db_models import RoleDBModel
from schema_models import RoleSchemaModel
from mutation_role import RoleInput

class CreateRole(graphene.Mutation):
    class Arguments():
        roleData = RoleInput(required=True)

    role = graphene.Field(RoleSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, roleData):

        import utils
        if utils.isAllowAccess():

            roleCode = roleData.roleCode
            roleDesc = roleData.roleDesc

            result = CreateRole()
            result.status = False

            from mutation_role import isRoleByRoleCodeExist

            if isRoleByRoleCodeExist(roleCode, info) is False:
                # can create
                newRole = RoleDBModel()
                newRole.roleCode = roleCode
                newRole.role_desc = roleDesc

                db_session.add(newRole)
                db_session.commit()

                result.role = newRole
                result.status = True
                result.msg = 'Create role with roleCode \'{}\' success.'.format(roleCode)

            else:
                # can't
                result.msg = 'This roleCode \'{}\' is exist.'.format(roleCode)

            return result


class CreateRoleMutation(graphene.ObjectType):
    roleCreate = CreateRole.Field(RoleSchemaModel)
