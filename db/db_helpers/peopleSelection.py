import utils
from db_models import PeopleDBModel
from schema_models import PeopleSchemaModel

def selectPeopleByPCode(peopleCode, ctx):
    query = PeopleSchemaModel.get_query(ctx)
    people = query.filter(PeopleDBModel.peopleCode == peopleCode).first()

    return people

def isPeopleByPCodeExist(pCode, ctx):
    people = selectPeopleByPCode(pCode, ctx)
    return type(people) is PeopleDBModel


from schema_models import (
    PeoplePosRoleSchemaModel,
    PositionSchemaModel
)
from db_models import (
    PeoplePosRoleDBModel,
    PositionDBModel
)

def selectPositionInPeopleByPeopleCode(peopleCode, ctx):
    query = PeoplePosRoleSchemaModel.get_query(ctx)
    peoplePosRoleObj = query.filter(PeoplePosRoleDBModel.peopleCode == peopleCode).first()

    if peoplePosRoleObj:
        getPositionQuery = PositionSchemaModel.get_query(ctx)
        return getPositionQuery.filter(PositionDBModel.posCode == peoplePosRoleObj.posCode).first()
    else:
        return None
