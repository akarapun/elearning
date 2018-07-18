import graphene
from mutation_people import PeopleInput

from db import db_session
from db_models import PeopleDBModel
from schema_models import PeopleSchemaModel

class CreatePeople(graphene.Mutation):
    class Arguments():
        peopleData = PeopleInput(required=True)

    # return field
    ok = graphene.Boolean()
    msg = graphene.NonNull(graphene.String)
    people = graphene.Field(PeopleSchemaModel)

    def mutate(self, info, peopleData):

        import utils
        if utils.isAllowAccess():

            toAddPeople = None
            ok = False
            msg = 'The pCode: {} is already exist.'.format(peopleData.peopleCode)

            # import db helper
            from db_helpers.peopleSelection import isPeopleByPCodeExist

            if isPeopleByPCodeExist(peopleData.peopleCode, info) is not True:
                toAddPeople = PeopleDBModel(
                    peopleCode=peopleData.peopleCode,
                    firstname=peopleData.firstname,
                    lastname=peopleData.lastname,
                    phone=peopleData.phone,
                    sexId=peopleData.sexId
                )

                db_session.add(toAddPeople)
                db_session.commit()

                ok = True
                msg = 'Create People\s pCode: {} success.'.format(toAddPeople.peopleCode)

            return CreatePeople(
                people=toAddPeople,
                ok=ok,
                msg=msg)
                

class CreatePeopleMutation(graphene.ObjectType):
    peopleCreate = CreatePeople.Field(PeopleSchemaModel)
