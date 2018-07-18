import graphene
import schema_models

class Position(graphene.ObjectType):
    posCode = graphene.String()
    posDesc = graphene.String()

class PositionInfo(graphene.ObjectType):
    totalCount = graphene.Int(default_value=10)
    positionInfo = graphene.Field(Position)

class People(graphene.ObjectType):
    peopleCode = graphene.String()
    firstname = graphene.String()
    lastname = graphene.String()
    sexId = graphene.String()
    phone = graphene.String()
    ext = graphene.String()
    createdAt = graphene.String()
    createdBy = graphene.String()
    updatedAt = graphene.String()
    updatedBy = graphene.String()

class IndividualPeople(People, graphene.ObjectType):
    position = graphene.Field(schema_models.PositionSchemaModel)
