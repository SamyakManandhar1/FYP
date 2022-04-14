from django.shortcuts import render
from django.shortcuts import redirect, render

from authentications.auth import employee_only
from django.contrib.auth.decorators import login_required
from employee.forms import ProfileForm
from django.contrib import messages

# Create your views here.

# @login_required
# @employee_only
def employeeDashboard(request):
    return render(request, "employee/employeeDashboard.html")


# @login_required
# @employee_only
def employeeProfile(request):
    return render(request, "employee/employeeProfile.html")


# @login_required
# @employee_only
def employeeUpdateProfile(request):
    profile = request.user.profile
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile updated successfully")
            return redirect('/employee/employeeprofile')
    context = {
        'profile': profile,
        'profileUpdateForm': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, "employee/employeeUpdateProfile.html", context)


# @login_required
# @employee_only
def leave(request):
    return render(request, "employee/leave.html")


# @login_required
# @employee_only
def attendance(request):
    return render(request, "employee/attendance.html")
