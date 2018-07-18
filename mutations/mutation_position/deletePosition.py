import graphene

from db import db_session
from db_models import PositionDBModel
from schema_models import PositionSchemaModel

class DeletePosition(graphene.Mutation):
    class Arguments():
        posCode = graphene.String(required=True)

    posCode = graphene.String()
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, posCode):

        import utils
        if utils.isAllowAccess():

            result = DeletePosition()
            result.status = False

            from mutation_position import selectPositionByPosCode, isPositionByPosCodeExist

            if isPositionByPosCodeExist(posCode, info):
                # can delete
                pos = selectPositionByPosCode(posCode, info)

                db_session.delete(pos)
                db_session.commit()

                result.posCode = posCode
                result.status = True
                result.msg = 'Delete position\'s posCode \'{}\' success.'.format(posCode)
            else:
                # can't
                result.msg = 'Can\'t find this posCode \'{}\''.format(posCode)

            return result

class DeletePositionMutation(graphene.ObjectType):
    positionDelete = DeletePosition.Field(PositionSchemaModel)
