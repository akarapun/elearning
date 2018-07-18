from sqlalchemy import or_

from db_models import PeoplePosRoleDBModel
from schema_models import PeoplePosRoleSchemaModel
import utils

def selectPeoplePosRole(params, ctx):

    peopleCode = params.peopleCode if hasattr(params, 'peopleCode') else ''
    posCode = params.posCode if hasattr(params, 'posCode') else ''
    roleCode = params.roleCode if hasattr(params, 'roleCode') else ''

    # utils.log('peopleCode: {}, posCode: {}, roleCode: {}'.format(peopleCode, posCode, roleCode))

    query = PeoplePosRoleSchemaModel.get_query(ctx)
    peoplePosRole = query.filter(or_(
        PeoplePosRoleDBModel.peopleCode == peopleCode,
        PeoplePosRoleDBModel.posCode == posCode,
        PeoplePosRoleDBModel.roleCode == roleCode
    )).first()

    # utils.log(peoplePosRole.peopleCode)
    # utils.log(peoplePosRole.posCode)
    # utils.log(peoplePosRole.roleCode)

    return peoplePosRole

def isPeoplePosRoleExist(params, ctx):
    peoplePosRole = selectPeoplePosRole(params, ctx)
    return type(peoplePosRole) is PeoplePosRoleDBModel
