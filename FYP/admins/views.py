from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib.auth.models import User
from admins.models import Employee,Department

# Create your views here.


@login_required
@admin_only
def adminDashboard(request):
    users = User.objects.all()
    employee = Employee.objects.all()
    department = Department.objects.all()
    
    employee_count = employee.count()
    department_count = department.count()
    admin_count = users.filter(is_superuser=1).count()

    context = {
        'totalEmployee': employee_count,
        'totalAdmin': admin_count,
        'totalDepartment': department_count,
        'activate_dashboard': 'active bg-dark'

    }

    return render(request, 'admins/adminDashboard.html', context)
