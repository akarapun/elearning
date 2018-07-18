import graphene

from db import db_session
from query_organization import Org
from db_models import OrganizationDBModel

class GetAllOrg(graphene.ObjectType):
    organization = graphene.List(Org)

    def resolve_organization(self, info):

        import utils
        if utils.isAllowAccess():
            orgs = db_session.query(OrganizationDBModel).all()

            return orgs
