from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=127, unique=True, blank=False, null=False)

    
