import graphene

from mutation_credential.createPeopleCredential import CreatePeopleCredentialMutation
from mutation_credential.updatePeopleCredential import UpdatePeopleCredentialMutation
from mutation_credential.deletePeopleCredential import DeletePeopleCredentialMutation

class PeopleCredentialMutation(
    CreatePeopleCredentialMutation,
    UpdatePeopleCredentialMutation,
    DeletePeopleCredentialMutation,
    graphene.ObjectType):
    pass