from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .manager import UserManager

class User(AbstractBaseUser):
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    secondery_password=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS=['phone_number','name']
    USERNAME_FIELD='email'

    objects=UserManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
