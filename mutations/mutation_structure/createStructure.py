import graphene
from db import db_session
from db_models import StructureDBModel
from mutation_structure import (CreateStructureInput, Structure)

class CreateStructure(graphene.Mutation):
    class Arguments():
        input = CreateStructureInput(required=True)

    structure = graphene.Field(Structure)
    status = graphene.Boolean(default_value=True)
    msg = graphene.String()

    def mutate(self, info, input):

        import utils
        if utils.isAllowAccess():
            strCode = input.strCode

            result = CreateStructure()

            from db_helpers.structureSelection import isStructureByStrCodeExist
            if isStructureByStrCodeExist(strCode):
                # Can't save
                result.msg = "This Structure with strCode '{}' is exist.".format(strCode)
            else:
                # Let create new Structure
                from datetime import datetime

                newStr = StructureDBModel(
                    strCode=strCode,
                    strDesc=input.strDesc,
                    createdAt=datetime.now(),
                    createdBy=input.createdBy
                )

                db_session.add(newStr)
                db_session.commit()

                result.structure = newStr
                result.status = True

            return result

class CreateStructureMutation(graphene.ObjectType):
    structureCreate = CreateStructure.Field()
