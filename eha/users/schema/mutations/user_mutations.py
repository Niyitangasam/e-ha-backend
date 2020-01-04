import graphene

class CreateUser(graphene.Mutation):
    """
      Mutation to create a new user
    """
    
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        profile_image = graphene.String()
        password = graphene.String(required=True)

    def mutate(self, info, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        mobile_number = kwargs.get('mobile_number')
        profile_image = kwargs.get('profile_image')
        password = kwargs.get('password')