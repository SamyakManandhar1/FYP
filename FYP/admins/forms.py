from django import forms
from django.forms import ModelForm
from .models import Department
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class AddEmployee(UserCreationForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password','is_staff']


# class ProfileForm(ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['phone','address','city','profile_pic']




# class AddEmployeeForm(ModelForm):
#     class Meta:
#         model = Department
#         fields = "__all__"
    