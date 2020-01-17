import graphene

from eha.apps.users.schema import AuthMutation

class Mutation(AuthMutation, graphene.ObjectType):
    pass
schema = graphene.Schema(mutation=Mutation)
