from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomManager

# Structure of the model of the user profile table
# AbstractBaseUser handles the actual authentication
# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50, null=False)
    is_staff = models.BooleanField(default=False, null=False)

    USERNAME_FIELD = 'email'
    objects = CustomManager()

    # def __str__(self) -> str:
    #     return self.full_name