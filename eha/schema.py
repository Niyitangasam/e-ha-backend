import graphene

from eha.users.schema import AuthMutation

class Mutation(AuthMutation, graphene.ObjectType):
    pass
schema = graphene.Schema(mutation=Mutation)
