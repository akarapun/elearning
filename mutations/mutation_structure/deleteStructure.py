import graphene

from db import db_session
from db_models import StructureDBModel

class DeleteStructure(graphene.Mutation):
    class Arguments():
        strCode = graphene.String(required=True)

    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

    def mutate(self, info, strCode):

        import utils
        if utils.isAllowAccess():
            result = DeleteStructure()

            from db_helpers.structureSelection import deleteStructureByStrCode
            if deleteStructureByStrCode(strCode):
                result.status = True
                result.msg = "Delete Structure with strCode '{}' success.".format(strCode)
            else:
                result.msg = "Can't find strCode '{}'.".format(strCode)

            return result

class DeleteStructureMutation(graphene.ObjectType):
    structureDelete = DeleteStructure.Field()
