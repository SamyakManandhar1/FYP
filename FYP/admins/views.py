from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib.auth.models import User
from admins.models import Employee,Department
from django.contrib import messages
# Create your views here.


@login_required
@admin_only
def adminDashboard(request):
    users = User.objects.all()
    employee = User.objects.all()
    department = Department.objects.all()
    
    employee_count = employee.filter(is_superuser=0).count()
    department_count = department.count()
    admin_count = users.filter(is_superuser=1).count()
    adminInfo =  users.filter(is_superuser=1)
    employeeInfo = users.filter(is_superuser=0)

    context = {
        'totalEmployee': employee_count,
        'totalAdmin': admin_count,
        "admin_info":adminInfo,
        "employee_info":employeeInfo,
        'totalDepartment': department_count,
        'activate_dashboard': 'active bg-dark'

    }

    return render(request, 'admins/adminDashboard.html', context)


# @login_required
# @admin_only
def allAdmins(request):
    admins = User.objects.filter(is_superuser=1).order_by('-id')
    context = {
        'admins': admins,
        'activate_admins': 'active bg-dark'

    }
    return render(request, 'admins/allAdmins.html', context)


@login_required
@admin_only
def demoteToEmployee(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = False
    user.is_superuser = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User Demoted to Customer Successfully!')
    return redirect('/admins/alladmins')

@login_required
@admin_only
def deactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Account Deactivated!')
    return redirect('/admins/alladmins')

@login_required
@admin_only
def reactivate(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'Admin Account Reactivated!')
    return redirect('/admins/alladmins')

