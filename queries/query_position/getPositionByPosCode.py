import graphene

from schema_models import PositionSchemaModel
from db_models import PositionDBModel
from db_helpers.positionSelection import selectPositionByPosCode, isPositionByPosCodeExist

class GetPositionByPosCodeReturnFields(graphene.ObjectType):
    position = graphene.Field(PositionSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

class GetPositionByPosCode(graphene.ObjectType):
    positionByPosCode = graphene.Field(
            GetPositionByPosCodeReturnFields, 
            posCode=graphene.String())

    def resolve_getPositionByPosCode(self, info, posCode):

        import utils
        if utils.isAllowAccess():

            result = GetPositionByPosCodeReturnFields()
            result.status = False

            pos = selectPositionByPosCode(posCode, info)
            if pos is not None:
                result.position = pos
                result.status = True
            else:
                result.msg = 'Can\'t find this posCode \'{}\'.'.format(posCode)

            return result
