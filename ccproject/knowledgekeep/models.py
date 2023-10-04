from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomManager
from django.core.exceptions import ValidationError

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

# YET TO MIGRATE
# def validate_paper_type(value):
#     from os import path
#     ext = path.splitext(value.name)[1]

#     if ext.lower() != '.pdf':
#         raise ValidationError('Only .pdf files are allowed')

# class Papers(models.Model):
#     type_choices = (
#         ('journal', 'Journal'),
#         ('article', 'Article')
#     )
#     id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     reviewed = models.BooleanField(default=False, null=False)
#     views = models.IntegerField(default=0)
#     paper_name = models.CharField(null=True, max_length=255)
#     paper_description = models.TextField()
#     added_on = models.DateTimeField(auto_now_add=True)
#     is_published = models.BooleanField(default=False)
#     updated_on = models.DateTimeField(auto_now=True)
#     file = models.FileField(upload_to="media/%Y/%m/%d", null=False, help_text="Upload only .pdf files.", validators=[validate_paper_type])
#     type = models.CharField(choices=type_choices, max_length=20, default='journal')