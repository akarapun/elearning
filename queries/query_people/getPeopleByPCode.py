import graphene

from db_models import PeopleDBModel
from schema_models import PeopleSchemaModel
from query_people import People, IndividualPeople, Position
import utils

class GetPeopleByPcodeReturnField(graphene.ObjectType):
    # people = graphene.Field(People)
    people = graphene.Field(IndividualPeople)
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

class GetPeopleByPcode(graphene.ObjectType):
    peopleByPeopleCode = graphene.Field(GetPeopleByPcodeReturnField, peopleCode=graphene.String())

    def resolve_peopleByPeopleCode(self, info, peopleCode):

        if utils.isAllowAccess():
            query = PeopleSchemaModel.get_query(info)
            people = query.filter(PeopleDBModel.peopleCode == peopleCode).first()

            result = GetPeopleByPcodeReturnField()
            if people is not None:

                # get position in people
                from db_helpers.peopleSelection import selectPositionInPeopleByPeopleCode
                posInPeople = selectPositionInPeopleByPeopleCode(people.peopleCode, info)

                result.status = True
                result.people = people

                # add position into people
                result.people.position = posInPeople
            else:
                result.msg = 'This p_code is not exist.'

            return result
