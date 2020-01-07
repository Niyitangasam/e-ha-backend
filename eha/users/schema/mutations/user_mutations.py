import graphene
from eha.users.models import User
from eha.users.schema.types.user_type import UserType

class CreateUser(graphene.Mutation):
    """
      Mutation to create a new user
    """

    user = graphene.Field(UserType)
    
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        mobile_number = graphene.String(required=True)
        profile_image = graphene.String()
        password = graphene.String(required=True)
        
    success = graphene.List(graphene.String)
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        
        try:
          user = User.objects.create_user(**kwargs)
          
          success = ['You have successfully registered']
          return CreateUser(success=success, user=user)
        except Exception as e:
            errors = ["Something went wrong: {}".format(e)]
            return CreateUser(errors=errors)