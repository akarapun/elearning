import graphene

from db import db_session
from db_models import PositionDBModel
from schema_models import PositionSchemaModel
from mutation_position import PositionInput

class CreatePosition(graphene.Mutation):
    class Arguments():
        positionData = PositionInput(required=True)

    position = graphene.Field(PositionSchemaModel)
    status = graphene.Boolean()
    msg = graphene.String()

    def mutate(self, info, positionData):

        import utils
        if utils.isAllowAccess():

            from mutation_position import isPositionByPosCodeExist

            newPos = None
            status = False
            msg = 'This posCode \'{}\' is exist.'.format(positionData.posCode)

            if isPositionByPosCodeExist(positionData.posCode, info) is False:
                newPos = PositionDBModel()
                newPos.posCode = positionData.posCode
                newPos.pos_desc = positionData.pos_desc

                db_session.add(newPos)
                db_session.commit()

                status = True
                msg = 'Create position\'s posCode {} success.'.format(positionData.posCode)

            return CreatePosition(
                position=newPos,
                status=status,
                msg=msg
            )
            

class CreatePositionMutation(graphene.ObjectType):
    positionCreate = CreatePosition.Field(PositionSchemaModel)
