from django.contrib.auth.base_user import BaseUserManager

# How the data need to be stored
class CustomManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email: raise ValueError('Email Requried')
        email = self.normalize_email(email=email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        return self.create_user(email, password, **extra_fields)