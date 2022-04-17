from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser



class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(max_length=1000,null=True,blank=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    
    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=10, null=True)
    department = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=300, null=True)
    city = models.CharField(max_length=100, null=True)
    profile_pic = models.FileField(
        upload_to='static/uploads', default='static/images/user.png')
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username




# class User(AbstractUser):

#     name = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

# class Employee(models.Model):
#     # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     department = models.CharField(max_length=50, null=True)


# class Employee(models.Model):
#     LANGUAGE = (('english', 'ENGLISH'),
#                 ('nepali', 'NEPALI'), ('hindi', 'HINDI'))
#     GENDER = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
#     emp_id = models.CharField(
#         max_length=70, default='emp'+str(random.randrange(100, 999, 1)))
#     emp_image = models.ImageField(blank=True, null=True)
#     first_name = models.CharField(max_length=50, null=False)
#     last_name = models.CharField(max_length=50, null=False)
#     mobile = models.CharField(max_length=15)
#     email = models.EmailField(max_length=125, null=False)
#     address = models.TextField(max_length=100, default='')
#     gender = models.CharField(choices=GENDER, max_length=10)
#     department = models.ForeignKey(
#         Department, on_delete=models.SET_NULL, null=True)
#     joined = models.DateTimeField(default=timezone.now)
#     language = models.CharField(
#         choices=LANGUAGE, max_length=10, default='english')
#     accnum = models.CharField(max_length=10, default='0123456789')
#     bank = models.CharField(max_length=25, default='First Bank Plc')
#     salary = models.CharField(max_length=16, default='00,000.00')

#     def __str__(self):
#         return self.first_name


# class Attendance (models.Model):
#     STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
#     date = models.DateField(auto_now_add=True)
#     first_in = models.TimeField()
#     last_out = models.TimeField(null=True)
#     status = models.CharField(choices=STATUS, max_length=15 )
#     staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

#     def save(self,*args, **kwargs):
#         self.first_in = timezone.localtime()
#         super(Attendance,self).save(*args, **kwargs)
        
        
        
        
# class CustomUser(AbstractUser):
#     is_student = models.BooleanField(default=False,null=True)


        

class CustomUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self) :
        return self.user.username