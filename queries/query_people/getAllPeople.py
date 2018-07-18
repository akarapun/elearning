import graphene
from schema_models import PeopleSchemaModel
from schema_models import PositionSchemaModel

class GetAllPeople(graphene.ObjectType):
    people = graphene.List(PeopleSchemaModel)

    def resolve_people(self, info):

        import utils
        if utils.isAllowAccess():
            query = PeopleSchemaModel.get_query(info)
            return query.all()
