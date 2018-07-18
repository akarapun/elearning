import graphene

from db import db_session
from db_models import RoleDBModel
from schema_models import RoleSchemaModel
from mutation_role import RoleInput

from datetime import datetime

class UpdateRole(graphene.Mutation):
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
            updatedBy = roleData.updatedBy

            result = UpdateRole()
            result.status = False

            from mutation_role import isRoleByRoleCodeExist, selectRoleByRoleCode

            if isRoleByRoleCodeExist(roleCode, info):
                # can update
                role = selectRoleByRoleCode(roleCode, info)
                role.role_desc = roleDesc
                role.updated_at = datetime.now()
                role.updated_by = updatedBy

                db_session.commit()

                result.role = role
                result.status = True
                result.msg = 'Update role with roleCode \'{}\' success.'.format(roleCode)

            else:
                # can't
                result.msg = 'Can\' find roleCode \'{}\'.'.format(roleCode)

            return result


class UpdateRoleMutation(graphene.ObjectType):
    roleUpdate = UpdateRole.Field(RoleSchemaModel)
