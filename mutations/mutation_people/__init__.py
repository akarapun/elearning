import graphene
# import db helper
from db_helpers.peopleSelection import isPeopleByPCodeExist, selectPeopleByPCode

class PeopleInput(graphene.InputObjectType):
    peopleCode = graphene.String(required=True)
    firstname = graphene.String()
    lastname = graphene.String()
    phone = graphene.String()
    sexId = graphene.Int()
    ext = graphene.String()