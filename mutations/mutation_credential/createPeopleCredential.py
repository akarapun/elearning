import graphene

from db import db_session
from schema_models import PeopleCredentialSchemaModel
from db_models import PeopleCredentialDBModel

class CredentialInput(graphene.InputObjectType):
    peopleCode = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)

class CreatePeopleCredential(graphene.Mutation):
    class Arguments():
        credentialData = CredentialInput(required=True)

    peopleCredential = graphene.Field(PeopleCredentialSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, credentialData):

        import utils
        if utils.isAllowAccess():
            
            from hashlib import sha256
            from settings.app import ENCODE_SECRET

            from db_helpers.peopleSelection import isPeopleByPCodeExist
            from db_helpers.peopleCredentialSelection import selectPeopleCredentialByPeople, isPeopleCredentialByPeopleCodeExist

            peopleCode = credentialData.peopleCode
            email = credentialData.email
            password = credentialData.password.encode('utf-8')
            hashedPassword = sha256(password).hexdigest()

            result = CreatePeopleCredential()
            result.status = False

            if isPeopleByPCodeExist(peopleCode, info):
                # found peopleCode
                # mean user is already add this people.

                # ask in PeopleCredentialTable that peopleCode is exist or not.
                if isPeopleCredentialByPeopleCodeExist(peopleCode, info) is False:

                    # peopleCode is not exist in PeopleCreatial table
                    # let's insert

                    newCredential = PeopleCredentialDBModel(
                        peopleCode=peopleCode,
                        email=email,
                        password=hashedPassword
                    )

                    db_session.add(newCredential)
                    db_session.commit()

                    result.peopleCredential = newCredential
                    result.status = True
                    result.msg = 'Create people\'s credential success.'

                else:
                    result.msg = 'This peopleCode \'{}\' is already exist.'.format(peopleCode)

            else:
                # this peopleCode is not exist. [need to add create new people first]
                result.msg = 'Can\'t find this peopleCode \''+ peopleCode +'\'.'
                result.msg += ' You need to create new People first.'

            return result


class CreatePeopleCredentialMutation(graphene.ObjectType):
    peopleCredentialCreate = CreatePeopleCredential.Field(PeopleCredentialSchemaModel)
