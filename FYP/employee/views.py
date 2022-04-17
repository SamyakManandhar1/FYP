from django.shortcuts import render
from django.shortcuts import redirect, render

from authentications.auth import employee_only
from django.contrib.auth.decorators import login_required
from employee.forms import ProfileForm, LeaveForm,AttendanceForm
from django.contrib import messages
from .models import Leave,Attendance

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage
from admins.models import CustomUser

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
    
    leaveInfo = Leave.objects.filter(user=CustomUser.objects.get(
        user=user)).order_by('-id')
    
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            user=request.user
            print(user.username)
            print(user.first_name)
            start = request.POST['start']
            end = request.POST['end']
            print(request.POST)
            leavetype = request.POST['leavetype']
            reson = request.POST['reason']
            lv = Leave(user=CustomUser.objects.get(user=user),start=start,end=end,status="Not Approved",leavetype=leavetype,reason=reson)
            lv.save()
            messages.add_message(request, messages.SUCCESS, ' Leave Applied Successfully')
            return redirect("/employee/leave")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to complete request! ')
            return render(request, 'employee/leave.html', {'form_leave': form})
    context = {
        'form_leave': LeaveForm,
        'leaves': leaveInfo,
        'activate_leave': 'active bg-primary',
    }
    return render(request, "employee/leave.html",context)



@login_required
# @employee_only
def attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            user = request.user
            first_in = request.POST['first_in']
            status = request.POST['status']
            attendance = Attendance(staff=CustomUser.objects.get(user=user),
                        first_in=first_in, status=status)
            attendance.save()
            
            messages.add_message(request, messages.SUCCESS,
                                 ' Attendance Completed Successfully')
            return redirect("/employee/attendance")
        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to complete request! ')
            return render(request, 'employee/attendance.html', {'attendance': form})
    
    
    context = {
    'attendance': AttendanceForm, 
    'activate_attendance': 'active bg-primary'    
    }
    return render(request, "employee/attendance.html", context)
