from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employee(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name= models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    joined_on=models.DateTimeField(auto_now=True)
