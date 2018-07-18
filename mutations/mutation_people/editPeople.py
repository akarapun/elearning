import graphene
from mutation_people import PeopleInput

from db import db_session
from db_models import PeopleDBModel
from schema_models import PeopleSchemaModel

class EditPeople(graphene.Mutation):
    class Arguments():
        editData = PeopleInput(required=True)

    people = graphene.Field(PeopleSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, editData):

        import utils
        if utils.isAllowAccess():
            
            toEditPeople = None

            status = False
            msg = ''

            from mutation_people import isPeopleByPCodeExist
            from db_helpers.peopleSelection import selectPeopleByPCode
            from db_helpers.peopleCredentialSelection import selectPeopleCredentialByPeopleCode

            if isPeopleByPCodeExist(editData.peopleCode, info):
                edittingPeople = selectPeopleByPCode(editData.peopleCode, info)
                edittingPeople.firstname = editData.firstname
                edittingPeople.lastname = editData.lastname
                edittingPeople.phone = editData.phone
                edittingPeople.sexId = editData.sexId

                db_session.commit()

                toEditPeople = edittingPeople
                status = True
                msg = 'update pCode\'s {} success.'.format(editData.peopleCode)
            else:
                msg = 'This pCode\'s {} is not exist'.format(editData.peopleCode)


        return EditPeople(
                people=toEditPeople,
                status=status,
                msg=msg)


class EditPeopleMutation(graphene.ObjectType):
    peopleEdit = EditPeople.Field(PeopleSchemaModel)
