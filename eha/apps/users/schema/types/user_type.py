import graphene
from graphene_django import DjangoObjectType

from eha.apps.users.models import User

class UserType(DjangoObjectType):
    
    class Meta:
        model = User
        exclude_fields = ['password']