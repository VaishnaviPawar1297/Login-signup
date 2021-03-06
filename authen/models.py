from django.db import models
from django.contrib.auth.models import AbstractUser
 
 # Create your models here.
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100, blank=False)
    age = models.PositiveIntegerField(null=True, blank=True)
    email=models.EmailField(blank=True, max_length=254, verbose_name='email address')
    
  