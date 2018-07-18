import graphene
from schema_models import PositionSchemaModel


class GetAllPosition(graphene.ObjectType):
    position = graphene.List(PositionSchemaModel)

    def resolve_position(self, info):

        import utils
        if utils.isAllowAccess():
            query = PositionSchemaModel.get_query(info)
            return query.all()
