
from django import forms

from admins.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['department','email','phone', 'address','city','profile_pic']