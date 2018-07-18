import graphene
from query_people.getAllPeople import GetAllPeople
from query_people.getPeopleByPCode import GetPeopleByPcode

from query_position.queries import PositionQueries
from query_role.queries import RoleQueries
from query_organization.query import OrganizationQuery

from queries.structure._query import StructureQueries

class RootQuery(
    GetPeopleByPcode,
    GetAllPeople,
    PositionQueries,
    RoleQueries,
    OrganizationQuery,
    StructureQueries,
    graphene.ObjectType):
    pass
