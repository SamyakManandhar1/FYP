from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
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
    


class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),
              ('LATE', 'LATE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15)
    staff = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance, self).save(*args, **kwargs)

    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)


