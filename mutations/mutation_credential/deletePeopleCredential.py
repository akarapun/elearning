import graphene

from db import db_session
from schema_models import PeopleCredentialSchemaModel
from db_models import PeopleCredentialDBModel
from db_helpers.peopleCredentialSelection import isPeopleCredentialByPeopleCodeExist, selectPeopleCredentialByPeople

class DeletePeopleCredential(graphene.Mutation):
    class Arguments():
        peopleCode = graphene.String(required=True)

    peopleCode = graphene.String()
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, peopleCode):

        import utils
        if utils.isAllowAccess():
            
            result = DeletePeopleCredential()

            if isPeopleCredentialByPeopleCodeExist(peopleCode, info):
                # can delete

                peopleCredential = selectPeopleCredentialByPeople(peopleCode, info)

                db_session.delete(peopleCredential)
                db_session.commit()

                result.peopleCode = peopleCode
                result.status = True
                result.msg = 'Delete peopleCredential\'s peopleCode \'{}\' success.'.format(peopleCode)

            else:
                # can't
                result.msg = 'Can\'t find this peopleCode \'{}\'.'.format(peopleCode)

            return result

class DeletePeopleCredentialMutation(graphene.ObjectType):
    peopleCredentialDelete = DeletePeopleCredential.Field(PeopleCredentialSchemaModel)
