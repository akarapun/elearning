import graphene

class PeoplePosRoleInput(graphene.InputObjectType):
    peopleCode = graphene.String()
    posCode = graphene.String()
    roleCode = graphene.String()
