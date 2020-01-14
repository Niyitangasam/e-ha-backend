import graphene

from .mutations.user_mutations import CreateUser

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()