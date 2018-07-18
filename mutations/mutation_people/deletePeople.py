import graphene

from db import db_session
from db_models import PeopleDBModel
from schema_models import PeopleSchemaModel

class DeletePeople(graphene.Mutation):
    class Arguments():
        peopleCode = graphene.NonNull(graphene.String)

    # return fields
    peopleCode = graphene.String()
    msg = graphene.String()
    status = graphene.Boolean()

    def mutate(self, info, peopleCode):

        import utils
        if utils.isAllowAccess():

            msg = ''
            status = False

            from mutation_people import isPeopleByPCodeExist, selectPeopleByPCode
            if isPeopleByPCodeExist(peopleCode, info):
                delettingPeople = selectPeopleByPCode(peopleCode, info)

                db_session.delete(delettingPeople)
                db_session.commit()

                status = True
                msg = 'delete pCode\'s {} success.'.format(peopleCode)
            else:
                msg = 'This pCode\'s {} is not exist'.format(peopleCode)

            return DeletePeople(
                peopleCode=peopleCode,
                msg=msg,
                status=status
            )


class DeletePeopleMutation(graphene.ObjectType):
    peopleDelete = DeletePeople.Field(PeopleSchemaModel)
