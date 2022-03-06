from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=400,unique=True)
    password  = models.CharField(max_length=200)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

# class Followers()