from django import forms
from django.contrib.auth.models import User 
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta: 
        model = Employee
        fields = ["username","password","email","full_name","address"]

        def clean_username(self):
            uname = self.cleaned_data.get("username")
            if User.objects.filter(username=uname).exists():
                raise forms.ValidationError("Seller with this Username already exist!!  Please use other Username")
            return uname

class EmployeeLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

