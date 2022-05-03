
import datetime
from .models import Leave
from django import forms
from admins.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['phone', 'address', 'city', 'profile_pic']


class LeaveForm (forms.ModelForm):

    class Meta:
        model = Leave
        fields = ['start', 'end', 'leavetype', 'reason']

        widgets = {
            'start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

        # widgets = {
        # 'first_in': forms.TimeField(required=True),
        # 'end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        # 'reason': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        # }


# class LeaveCreationForm(forms.ModelForm):
# 	reason = forms.CharField(
# 	    required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

# 	class Meta:
# 		model = Leave
# 		exclude = ['user', 'defaultdays', 'hrcomments',
#                     'status', 'is_approved', 'updated', 'created']

# 	def clean_enddate(self):
# 		enddate = self.cleaned_data['enddate']
# 		startdate = self.cleaned_data['startdate']
# 		today_date = datetime.date.today()

# 		if (startdate or enddate) < today_date:  # both dates must not be in the past
# 			raise forms.ValidationError(
# 			    "Selected dates are incorrect,please select again")

# 		elif startdate >= enddate:  # TRUE -> FUTURE DATE > PAST DATE,FALSE other wise
# 			raise forms.ValidationError("Selected dates are wrong")

# 		return enddate
