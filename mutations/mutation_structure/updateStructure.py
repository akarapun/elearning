import graphene
from db import db_session
from mutation_structure import UpdateStructureInput, Structure

class UpdateStructure(graphene.Mutation):
    class Arguments():
        input = UpdateStructureInput(required=True)

    structure = graphene.Field(Structure)
    status = graphene.Boolean(default_value=True)
    msg = graphene.String()

    def mutate(self, info, input):

        import utils
        if utils.isAllowAccess():
            strCode = input.strCode

            result = UpdateStructure()

            from db_helpers.structureSelection import isStructureByStrCodeExist, selectStructureByStrCode
            if isStructureByStrCodeExist(strCode):
                # let update
                from datetime import datetime

                toUpdateStr = selectStructureByStrCode(strCode)
                toUpdateStr.strDesc = input.strDesc
                toUpdateStr.updatedBy = input.updatedBy
                toUpdateStr.updatedAt = datetime.now()

                db_session.commit()

                result.structure = toUpdateStr
                result.status = True
                result.msg = "Update structure with strCode '{}' success.".format(strCode)
            else:
                result.msg = "Can't find strCode '{}'.".format(strCode)

            return result


class UpdateStructureMutation(graphene.ObjectType):
    structureUpdate = UpdateStructure.Field()
