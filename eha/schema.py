import graphene

import users.schema

class Mutation(users.schema.Mutation, graphene.ObjectType):
    pass
schema = graphene.Schema(mutation=Mutation)
