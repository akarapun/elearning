import graphene
from mutation_organization.create import OrgCreateMutation
from mutation_organization.delete import OrgDeleteMutation

class OrgMutations(
    OrgCreateMutation,
    OrgDeleteMutation,
    graphene.ObjectType):
    pass
