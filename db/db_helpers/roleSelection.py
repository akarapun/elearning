from db_models import RoleDBModel
from schema_models import RoleSchemaModel

def selectRoleByRoleCode(roleCode, ctx):
    query = RoleSchemaModel.get_query(ctx)
    role = query.filter(RoleDBModel.roleCode == roleCode).first()

    return role

def isRoleByRoleCodeExist(roleCode, ctx): 
    role = selectRoleByRoleCode(roleCode, ctx)
    return type(role) is RoleDBModel

