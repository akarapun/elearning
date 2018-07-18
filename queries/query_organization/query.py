import graphene

from query_organization.getAllOrg import GetAllOrg

class OrganizationQuery(
    GetAllOrg,
    graphene.ObjectType):
    pass
