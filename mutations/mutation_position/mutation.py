import graphene

from mutation_position.createPosition import CreatePositionMutation
from mutation_position.updatePosition import UpdatePositionMutation
from mutation_position.deletePosition import DeletePositionMutation

class PositionMutation(
    CreatePositionMutation,
    UpdatePositionMutation,
    DeletePositionMutation,
    graphene.ObjectType):
    pass