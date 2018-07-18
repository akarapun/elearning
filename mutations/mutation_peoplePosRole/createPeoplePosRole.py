import graphene

from db import db_session
from mutation_peoplePosRole import PeoplePosRoleInput
from db_models import PeoplePosRoleDBModel

class PeoplePosRoleSchemaModel(graphene.ObjectType):
    peopleCode = graphene.String()
    posCode = graphene.String()
    roleCode = graphene.String()

class CreatePeoplePosRole(graphene.Mutation):
    class Arguments():
        input = PeoplePosRoleInput(required=True)

    peoplePosRole = graphene.Field(PeoplePosRoleSchemaModel)
    status = graphene.String(default_value=False)
    msg = graphene.String()

    def mutate(self, info, input):

        import utils
        if utils.isAllowAccess():

            result = CreatePeoplePosRole()

            from db_helpers.peopleSelection import isPeopleByPCodeExist
            from db_helpers.positionSelection import isPositionByPosCodeExist
            from db_helpers.roleSelection import isRoleByRoleCodeExist

            from db_helpers.peoplePosRoleSelection import isPeoplePosRoleExist
            if isPeoplePosRoleExist(input, info) is False:

                # check peopleCode, positionCode, roleCode if they are exist or not ?
                if isPeopleByPCodeExist(input.peopleCode, info) and isPositionByPosCodeExist(input.posCode, info) and isRoleByRoleCodeExist(input.roleCode, info):

                    # let's save
                    newPeoplePosRole = PeoplePosRoleDBModel()
                    newPeoplePosRole.peopleCode = input.peopleCode
                    newPeoplePosRole.posCode = input.posCode
                    newPeoplePosRole.roleCode = input.roleCode

                    db_session.add(newPeoplePosRole)
                    db_session.commit()

                    result.peoplePosRole = newPeoplePosRole
                    result.status = True
                    result.msg = "Create peopleCode: {}, posCode: {}, roleCode: {} success.".format(input.peopleCode, input.posCode, input.roleCode)
                else:
                    result.msg = "Some if theme is not exist in their table."

            else:
                result.msg = "These peopleCode: {}, posCode: {}, roleCode: {} are exist.".format(
                        input.peopleCode,
                        input.posCode,
                        input.roleCode)

            return result


class CreatePeoplePosRoleMutation(graphene.ObjectType):
    peoplePosRoleCreate = CreatePeoplePosRole.Field()
