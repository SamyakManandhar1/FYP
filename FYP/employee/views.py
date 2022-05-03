from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from employee.forms import ProfileForm, LeaveForm
from django.contrib import messages
from admins.models import CustomUser
from .models import Leave
from admins.models import Attendance
# Create your views here.


# ===================================================
# ================== Employee Dashboard=============
# ===================================================
@login_required
def employeeDashboard(request):
    user = request.user
    leave = Leave.objects.filter(user_id=CustomUser.objects.get(
        user=user))
    myLeave = leave.count()
    attendance = Attendance.objects.filter(staff_id=CustomUser.objects.get(
        user=user))
    myAttendance = attendance.count()
    context={
        'myLeave':myLeave,
        'myAttendance':myAttendance,
        'activate_dashboard': 'active bg-primary',
        
    }
    return render(request, "employee/employeeDashboard.html",context)


# ===================================================
# ==================== PROFILE ================
# ===================================================

@login_required
def employeeProfile(request):
    context={
        'activate_profile': 'active bg-primary',
        
    }
    return render(request, "employee/employeeProfile.html",context)


@login_required
def employeeUpdateProfile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Profile updated successfully")
            return redirect('/employee/employeeprofile')
    context = {
        'profile': profile,
        'profileUpdateForm': ProfileForm(instance=profile),
        'activate_profile': 'active bg-primary',
    }
    return render(request, "employee/employeeUpdateProfile.html", context)


# ===================================================
# ================= Leave Employee ===============
# ===================================================

@login_required
def leave(request):
    user = request.user

    leaveInfo = Leave.objects.filter(user=CustomUser.objects.get(
        user=user)).order_by('-id')

    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            user = request.user
            start = request.POST['start']
            end = request.POST['end']
            leavetype = request.POST['leavetype']
            reson = request.POST['reason']
            lv = Leave(user=CustomUser.objects.get(user=user), start=start,
                        end=end, status="Not Approved", leavetype=leavetype, reason=reson)
            lv.save()
            messages.add_message(request, messages.SUCCESS,
                                    ' Leave Applied Successfully')
            return redirect("/employee/leave")
        else:
            messages.add_message(request, messages.ERROR,
                                    'Unable to complete request! ')
            return render(request, 'employee/leave.html', {'form_leave': form})
    context = {
        'form_leave': LeaveForm,
        'leaves': leaveInfo,
        'activate_leave': 'active bg-primary',
    }
    return render(request, "employee/leave.html", context)


# ===================================================
# ==================== Attendance ================
# ===================================================

@login_required
def attendance(request):
    user = request.user
    usr= CustomUser.objects.get(user=user)
    attendance = Attendance.objects.filter(staff=usr).order_by('-id')

    context = {
        'atten': attendance,
        'activate_attendance': 'active bg-primary'
    }
    return render(request, "employee/attendance.html", context)