import graphene

from mutation_auth.login import LoginMutation

class AuthenticationMutation(
    LoginMutation,
    graphene.ObjectType):
    pass