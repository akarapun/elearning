import graphene

from db import db_session
from mutation_position import PositionInput
from db_models import PositionDBModel
from schema_models import PositionSchemaModel

class UpdatePosition(graphene.Mutation):
    class Arguments():
        updateData = PositionInput(required=True)

    position = graphene.Field(PositionSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, updateData):

        import utils
        if utils.isAllowAccess():

            newPosCode = updateData.posCode
            newPosDesc = updateData.pos_desc

            from mutation_position import selectPositionByPosCode, isPositionByPosCodeExist

            result = UpdatePosition()
            result.status = False

            if isPositionByPosCodeExist(newPosCode, info):
                # can update
                pos = selectPositionByPosCode(newPosCode, info)
                pos.posCode = newPosCode
                pos.pos_desc = newPosDesc

                db_session.commit()

                result.status = True
                result.position = pos
                result.msg = 'Update Postion by posCode \'{}\' success.'.format(newPosCode)
            else:
                # can't
                result.msg = 'Can\'t find this posCode \'{}\'.'.format(newPosCode)

            return result


class UpdatePositionMutation(graphene.ObjectType):
    positionUpdate = UpdatePosition.Field(PositionSchemaModel)
