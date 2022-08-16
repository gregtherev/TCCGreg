from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """This is the raw custom user model for use in rank"""
    email = models.EmailField('E-mail', max_length=254, unique=True)
