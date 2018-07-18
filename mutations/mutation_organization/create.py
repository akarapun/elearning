import graphene
from db import db_session
from db_models import OrganizationDBModel
from mutation_organization import (
    OrgCreateInput,
    Org
)

class OrgCreate(graphene.Mutation):
    class Arguments():
        input = OrgCreateInput(required=True)

    org = graphene.Field(Org)
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, input):

        import utils
        if utils.isAllowAccess():
            result = OrgCreate()
            orgCode = input.orgCode

            from db_helpers.orgSelection import isOrgByOrgCodeExist
            if isOrgByOrgCodeExist(orgCode):
                result.msg = "This orgCode '{}' is exists.".format(orgCode)
            else:
                from datetime import datetime
                newOrg = OrganizationDBModel(
                    orgCode=orgCode,
                    strCode=input.strCode,
                    parentOrgCode=input.parentOrgCode,
                    orgTypeCode=input.orgTypeCode,
                    orgDesc=input.orgDesc,
                    createdAt=datetime.now(),
                    createdBy=input.createdBy)

                db_session.add(newOrg)
                db_session.commit()

                result.org = newOrg
                result.status = True
                result.msg = "Create Organization with orgCode '{}' success.".format(orgCode)

            return result


class OrgCreateMutation(graphene.ObjectType):
    organizationCreate = OrgCreate.Field()
