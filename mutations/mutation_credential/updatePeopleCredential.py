import graphene

from db import db_session
from schema_models import PeopleCredentialSchemaModel
from db_models import PeopleCredentialDBModel
from db_helpers.peopleCredentialSelection import selectPeopleCredentialByPeople, isPeopleCredentialByPeopleCodeExist
from db_helpers.peopleSelection import isPeopleByPCodeExist

class PeopleCredentialUpdateDataInput(graphene.InputObjectType):
    peopleCode = graphene.String(required=True)
    email = graphene.String()
    password = graphene.String(required=True)
    updatedBy = graphene.String(required=True)

class UpdatePeopleCredential(graphene.Mutation):
    class Arguments():
        updateData = PeopleCredentialUpdateDataInput(required=True)

    peopleCredential = graphene.Field(PeopleCredentialSchemaModel)
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, updateData):

        import utils
        if utils.isAllowAccess():
            
            peopleCode = updateData.peopleCode
            email = updateData.email
            password = updateData.password.encode('utf-8')
            updatedBy = updateData.updatedBy

            result = UpdatePeopleCredential()

            if isPeopleCredentialByPeopleCodeExist(peopleCode, info) and isPeopleByPCodeExist(peopleCode, info):
                # let's update

                from datetime import datetime
                now = datetime.now()

                import hashlib
                hashedPassword = hashlib.sha256(password).hexdigest()

                toUpdatePeopleCredential = selectPeopleCredentialByPeople(peopleCode, info)
                toUpdatePeopleCredential.email = email
                toUpdatePeopleCredential.password = hashedPassword
                toUpdatePeopleCredential.updated_at = now
                toUpdatePeopleCredential.updated_by = updatedBy

                db_session.commit()

                result.peopleCredential = toUpdatePeopleCredential
                result.status = True
                result.msg = 'Update peopleCredential with peopleCode \'{}\' success.'.format(peopleCode)
            else:
                # can't update
                result.msg = 'Can\'t find this peopleCode \'{}\'.'.format(peopleCode)

            return result


class UpdatePeopleCredentialMutation(graphene.ObjectType):
    peopleCredentialUpdate = UpdatePeopleCredential.Field(PeopleCredentialSchemaModel)
