import graphene

from eha.users.schema.mutations.user_mutations import CreateUser

class Mutation(CreateUser, graphene.ObjectType):
    pass
schema = graphene.Schema(mutation=Mutation)
