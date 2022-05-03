from django import forms
from django.forms import ModelForm
from .models import Department,Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"


class AddEmployee(UserCreationForm):
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','is_staff','password1']


class AttendanceForm (forms.ModelForm):

    class Meta:
        model = Attendance
        fields = "__all__"
        
        widgets = {
            'first_in': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            
        }


