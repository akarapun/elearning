import graphene

from db import db_session

class DeleteRole(graphene.Mutation):
    class Arguments():
        roleCode = graphene.String(required=True)

    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, roleCode):

        import utils
        if utils.isAllowAccess():

            result = DeleteRole()

            from db_helpers.roleSelection import selectRoleByRoleCode, isRoleByRoleCodeExist
            if isRoleByRoleCodeExist(roleCode, info):
                toDeleteRole = selectRoleByRoleCode(roleCode, info)

                db_session.delete(toDeleteRole)
                db_session.commit()

                result.status = True
                result.msg = "Delete Role with roleCode '{roleCode}' success."
            else:
                result.msg = "Can't find roleCode {roleCode}."

            return result


class DeleteRoleMutation(graphene.ObjectType):
    roleDelete = DeleteRole.Field()
