from db_models import PositionDBModel
from schema_models import PositionSchemaModel

def selectPositionByPosCode(posCode, ctx):
    query = PositionSchemaModel.get_query(ctx)
    pos = query.filter(PositionDBModel.posCode == posCode).first()

    return pos

def isPositionByPosCodeExist(posCode, ctx): 
    pos = selectPositionByPosCode(posCode, ctx)
    return type(pos) is PositionDBModel

