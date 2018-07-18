import graphene

from schema_models import RoleSchemaModel

class GetAllRole(graphene.ObjectType):
    role = graphene.List(RoleSchemaModel)

    def resolve_role(self, info):

        import utils
        if utils.isAllowAccess():
            query = RoleSchemaModel.get_query(info)
            return query.all()
