import graphene

from db import db_session
from schema_models import PeopleCredentialSchemaModel
from db_models import PeopleCredentialDBModel

import jwt

class LoginParams(graphene.InputObjectType):
    username = graphene.String(description='username or email.', required=True)
    password = graphene.String(required=True)

class Login(graphene.Mutation):
    class Arguments():
        params = LoginParams(required=True)

    status = graphene.Boolean(default_value=False)
    token = graphene.String()
    msg = graphene.String()

    def mutate(self, info, params):
        username = params.username
        password = params.password.encode('utf-8')

        # make encoded password

        import hashlib
        hashedPassword = hashlib.sha256(password).hexdigest()

        # filter by username and password

        query = PeopleCredentialSchemaModel.get_query(info)
        peopleCredential = query.filter(
            PeopleCredentialDBModel.username == username,
            PeopleCredentialDBModel.password == hashedPassword
        ).first()

        result = Login()

        # check if username and password are matched

        if peopleCredential is not None:

            # get loggin user's info

            from db_helpers.peopleSelection import selectPeopleByPCode
            loggedinUser = selectPeopleByPCode(peopleCredential.peopleCode, info)

            import datetime
            from settings.app import ENCODE_SECRET

            encoded = jwt.encode({
                'user': {
                    'peopleCode': peopleCredential.peopleCode,
                    'firstname': loggedinUser.firstname,
                    'lastname': loggedinUser.lastname
                },
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }, ENCODE_SECRET, algorithm='HS256')

            result.status = True
            result.token = encoded.decode('utf-8')
            result.msg = 'Login success.'
        else:
            result.msg = 'Username or password is invalid.'

        return result

class LoginMutation(graphene.ObjectType):
    login = Login.Field()
