from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from django.contrib.auth.models import BaseUserManager


class UserProfileMananger(BaseUserManager):
     
     def create_user(self, username, email, fullname, password=None):
          if not email:
               raise ValueError('You must provide an email address')
          
          email = self.normalize_email(email)
          user = self.model(email=email, fullname=fullname,username=username)
          user.set_password(password)
          user.save(using= self._db)
          return user
     
     def create_superuser(self, email, password, username ):
          user = self.create_user(email, password, username)
          user.is_superuser = True
          user.is_staff = True
          user.save(using=self._db)
          return user
               



class UserProfile(AbstractBaseUser):
     
     email = models.EmailField(max_length=255, unique=True)
     username = models.CharField(max_length=255, unique=True)
     fullname = models.CharField(max_length=255, unique=True)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)
     
     objects =UserProfileMananger()
     
     USERNAME_FIELD='username'
     
     REQUIRED_FIELDS=["email"]
     
     
     def __str__(self):
          
          return f"this account belongs to {self.username}"