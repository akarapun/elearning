import graphene

from query_position.getAllPositions import GetAllPosition
from query_position.getPositionByPosCode import GetPositionByPosCode

class PositionQueries(
    GetAllPosition,
    GetPositionByPosCode,
    graphene.ObjectType):
    pass