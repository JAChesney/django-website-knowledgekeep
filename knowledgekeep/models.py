from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomManager
from django.core.exceptions import ValidationError

# Structure of the model of the user profile table
# AbstractBaseUser handles the actual authentication
# Create your models here.

# class SubcriptionPlan(models.Model):
#     subcription_id = models.AutoField(primary_key=True)
#     subcription_type = models.CharField(max_length=20)
#     duration = models.IntegerField()


class UserProfile(AbstractBaseUser, PermissionsMixin):
    subsciption_choices = (
        ('3months', '3 Months'),
        ('6months', '6 Months'),
        ('1year', '1 Year')
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=50, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    has_subscribed = models.BooleanField(default=False, null=False)
    subscription_type = models.CharField(choices=subsciption_choices, max_length=20, null=True)
    subscribed_on = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomManager()

    # def __str__(self) -> str:
    #     return self.full_name

# YET TO MIGRATE
def validate_paper_type(value):
    from os import path
    ext = path.splitext(value.name)[1]

    if ext.lower() != '.pdf':
        raise ValidationError('Only .pdf files are allowed')

class Papers(models.Model):
    type_choices = (
        ('financeandeconomics', 'Finance & Economics'),
        ('mathematicsandstatistics', 'Mathematics and Statictics'),
        ('environmentalscience', 'Environmental Science'),
        ('computerscience', 'Computer Science')

    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    reviewed = models.BooleanField(default=False, null=False)
    
    views = models.IntegerField(default=0)
    paper_name = models.CharField(null=True, max_length=255)
    paper_description = models.TextField()
    short_description = models.TextField(null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="media/%Y/%m/%d", null=False, help_text="Upload only .pdf files.", validators=[validate_paper_type])
    type = models.CharField(choices=type_choices, max_length=25, default='Finance & Economics')

    def __str__(self) -> str:
        return self.paper_name
    


