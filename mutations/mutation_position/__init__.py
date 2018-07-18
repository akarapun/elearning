import graphene

from db_helpers.positionSelection import selectPositionByPosCode, isPositionByPosCodeExist

class PositionInput(graphene.InputObjectType):
    posCode = graphene.String(required=True)
    pos_desc = graphene.String()
    pass