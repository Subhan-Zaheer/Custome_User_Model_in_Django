from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import *

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=15)
    email = models.EmailField(unique=True, max_length=15)
    bio = models.EmailField(max_length=50)
    profile_photo = models.ImageField(upload_to='profile')

    USERNAME_FIELD = 'phone_number'
    obj = CustomManager()

    def __str__(self) -> str:
        return f" Phone number is : {self.phone_number}"
    

