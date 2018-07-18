import graphene
from queries.structure import IndividualStructure

class GetStructureByStrCodeResult(graphene.ObjectType):
    structure = graphene.Field(IndividualStructure)
    status = graphene.Boolean(default_value=False)
    msg = graphene.String()

class GetStructureByStrCode(graphene.ObjectType):
    structureBy = graphene.Field(GetStructureByStrCodeResult, strCode=graphene.String())

    def resolve_structureBy(self, info, strCode):

        import utils
        if utils.isAllowAccess():

            result = GetStructureByStrCodeResult()

            from db_helpers.structureSelection import (
                isStructureByStrCodeExist,
                selectStructureByStrCode)
            if isStructureByStrCodeExist(strCode):
                structure = selectStructureByStrCode(strCode)

                result.structure = structure
                result.status = True
            else:
                result.msg = "Can't find this strCode '{}'.".format(strCode)

            return result
