from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib.auth.models import User
from admins.models import Employee,Department
from django.contrib import messages

from .forms import DepartmentForm
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


# ===================================================
# ==================== DEPARTMENT CRUD ================
# ===================================================

@login_required
@admin_only
def allDepartment(request):
    department = Department.objects.all().order_by('-id')
    context = {
        'department': department,
        'activate_department': 'active bg-primary'
    }
    return render(request, 'admins/department.html', context)

@login_required
@admin_only
def departmentForm(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Department added Successfully')
            return redirect("/admins/department_form")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add Department')
            return render(request, 'admins/departmentForm.html', {'form_department': form})
    context = {
        'form_department': DepartmentForm,
        'activate_department': 'active bg-dark',
    }
    return render(request , 'admins/departmentForm.html', context)

@login_required
@admin_only
def getDepartment(request):
    departments = Department.objects.all().order_by('-id')
    context = {
        'departments': departments,
        'activate_department': 'active bg-dark'
    }
    return render(request, 'admins/getDepartment.html', context)

@login_required
@admin_only
def deleteDepartment(request,department_id):
    department = Department.objects.get(id=department_id)
    department.delete()
    messages.add_message(request, messages.SUCCESS, 'Department deleted successfully')
    return redirect('/admins/department')

@login_required
@admin_only
def departmentUpdateForm(request,department_id):
    department = Department.objects.get(id=department_id)
    if request.method == "POST":
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Department updated Successfully')
            return redirect("/admins/department")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update Department')
            return render(request, 'admins/departmentUpdateForm.html', {'form_department': form})

    context = {
        'form_department': DepartmentForm(instance=department),
        'activate_department': 'active bg-dark',
    }

    return render(request , 'admins/departmentUpdateForm.html', context)