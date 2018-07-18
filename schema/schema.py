import graphene
from root_query import RootQuery as query
from root_mutation import RootMutation as mutation

def get():
    return graphene.Schema(query=query, mutation=mutation)
