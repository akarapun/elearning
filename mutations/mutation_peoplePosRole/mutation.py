import graphene

from mutation_peoplePosRole.createPeoplePosRole import CreatePeoplePosRoleMutation

class PeoplePosRoleMutation(
    CreatePeoplePosRoleMutation,
    graphene.ObjectType):
    pass
