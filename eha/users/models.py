from django.db import models
from eha.manager import BaseManager
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from eha.utils.id_generators import ID_LENGTH, id_gen

class User(AbstractBaseUser, PermissionsMixin):
    """
       User Model
    """
    id = models.CharField(max_length=ID_LENGTH, primary_key=True, default=id_gen, editable=False)
    email = models.EmailField(max_length=100, unique=True)
    username = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100, null=True, unique=True)
    profile_image = models.URLField(
        default='https://res.cloudinary.com/health-id/image/upload/'
        'v1554552278/Profile_Picture_Placeholder.png'
    )

    USERNAME_FIELD = "username"

class UserManager(BaseUserManager, BaseManager):
    def create_user(self, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        mobile_number = kwargs.get('mobile_number')
        profile_image = kwargs.get('profile_image')
        password = kwargs.get('password')

        user = self.model.objects.filter(email=email).first()
        user_number = self.model.objects.filter(mobile_number=mobile_number).first()

        if user_number:
             raise ValueError(
                "User with mobile number {mobile_number} "
                "already exists".format(mobile_number=mobile_number)
            )
        if user:
            raise ValueError(
                "User with email {email} already exists".format(email=email)
            )