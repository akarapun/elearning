import graphene

from mutation_people.editPeople import EditPeopleMutation
from mutation_people.createPeople import CreatePeopleMutation
from mutation_people.deletePeople import DeletePeopleMutation

from mutation_position.mutation import PositionMutation
from mutation_role.mutation import RoleMutation

from mutation_credential.mutation import PeopleCredentialMutation

from mutation_auth.mutation import AuthenticationMutation

from mutation_peoplePosRole.mutation import PeoplePosRoleMutation

from mutation_organization.mutation import OrgMutations
from mutation_structure.mutation import StructureMutation

class RootMutation(
    CreatePeopleMutation,
    EditPeopleMutation,
    DeletePeopleMutation,
    PositionMutation,
    RoleMutation,
    PeopleCredentialMutation,
    AuthenticationMutation,
    PeoplePosRoleMutation,
    StructureMutation,
    graphene.ObjectType):
    pass
