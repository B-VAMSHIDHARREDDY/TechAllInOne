from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)

