import graphene

from db import db_session

class OrgDelete(graphene.Mutation):
    class Arguments():
        orgCode = graphene.String(required=True)

    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, orgCode):

        import utils
        if utils.isAllowAccess():
            result = OrgDelete()

            from db_models.orgSelection import isOrgByOrgCodeExist, selectOrgByOrgCode
            if isOrgByOrgCodeExist(orgCode):
                toDeleteOrg = selectOrgByOrgCode(orgCode)

                db_session.delete(toDeleteOrg)
                db_session.commit()

                result.status = True
                result.msg = "Delete organziation by orgCode '{}' success.".format(orgCode)
            else:
                result.msg = "Org by this orgCode '{}' is not exist.".format(orgCode)

            return result


class OrgDeleteMutation(graphene.ObjectType):
    organizationDelete = OrgDelete.Field()
