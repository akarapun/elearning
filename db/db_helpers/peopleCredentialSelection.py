from db_models import PeopleCredentialDBModel
from schema_models import PeopleCredentialSchemaModel

def selectPeopleCredentialByPeople(peopleCode, ctx):
    query = PeopleCredentialSchemaModel.get_query(ctx)
    peopleCredential = query.filter(PeopleCredentialDBModel.peopleCode == peopleCode).first()

    return peopleCredential

def isPeopleCredentialByPeopleCodeExist(peopleCode, ctx):
    peopleCredential = selectPeopleCredentialByPeople(peopleCode, ctx)
    return type(peopleCredential) is PeopleCredentialDBModel
