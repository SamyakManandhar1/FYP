from django.shortcuts import render
from django.shortcuts import redirect, render

from authentications.auth import employee_only
from django.contrib.auth.decorators import login_required
from employee.forms import ProfileForm,LeaveForm
from django.contrib import messages
from .models import Leave

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
# Create your views here.

@login_required
# @employee_only
def employeeDashboard(request):
    return render(request, "employee/employeeDashboard.html")


# @login_required
# @employee_only
def employeeProfile(request):
    return render(request, "employee/employeeProfile.html")


@login_required
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


@login_required
# @employee_only
def leave(request):
    user = request.user
    user_id= user.id
    print(user_id)
    
    leaveInfo = Leave.objects.filter(status="Approved").order_by('-id')
    
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            user=request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, ' Leave Applied Successfully')
            return redirect("/employee/leave")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to complete request! ')
            return render(request, 'employee/leave.html', {'form_leave': form})
    context = {
        'form_leave': LeaveForm,
        # 'leaves': leaveInfo,
        'activate_leave': 'active bg-primary',
    }
    return render(request, "employee/leave.html",context)



@login_required
# @employee_only
def attendance(request):
    return render(request, "employee/attendance.html")
