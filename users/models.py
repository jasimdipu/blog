from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.models import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):
    email = models.EmailField()
