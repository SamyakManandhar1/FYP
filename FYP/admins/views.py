from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from authentications.auth import admin_only
from django.contrib.auth.models import User
from admins.models import CustomUser, Department
from django.contrib import messages
from .models import Profile
from employee.models import Leave
from .forms import DepartmentForm,AddEmployee
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage

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
        'activate_dashboard': 'active bg-success'

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
# ==================== DEPARTMENT CRUD ==============
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
    print(department)
    department.delete()

    
    # employee.delete()
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



# ===================================================
# ==================== EMPLOYEE CRUD ================
# ===================================================
@login_required
@admin_only
def employee(request):
    users = User.objects.all()    
    employeeInfo = users.filter(is_superuser=0)
    print(CustomUser.objects.all())

    data = []
    for i in users:
        if not i.is_superuser:
        # data['first_name'] = i.first_name
        # data['last_name'] = i.last_name
        # data['username'] = i.username
        # data['email'] = i.email
        # data['is_employee'] = i.is_staff
        # data['joined_date'] = i.date_joined
        # print(i)
            dt = CustomUser.objects.get(user=i)
            print(dt.department)
            data.append(dt.department)
        # if 
        # data['dep'] = dt.department
    dt = zip(employeeInfo,data)
    context = {
        "employee_info":dt,
        'activate_employee': 'active bg-primary',
        'data':data

    }
    print("suman")
    return render(request, "admins/employee.html",context)


@login_required
@admin_only
def addEmployee(request):
    if request.method == 'POST':
        form = AddEmployee(request.POST)
        dep = request.POST['dep']
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')


        if form.is_valid():
            user = form.save()
            user.save()
            CustomUser.objects.create(user=user,department= dep)
            Profile.objects.create(
                user=user, username=user.username, department=dep, email=user.email,  first_name=user.first_name, last_name=user.last_name )
            
            template = render_to_string('admins/employeeAdd.html',
                                        {'username': username,'email': email, 'password': password})
            email = EmailMessage(
            'New Employee - Login Details',
            template, settings.EMAIL_HOST_USER, [email],
        )
            email.fail_silently = False
            print(request.user.email)
            email.send()
            messages.add_message(request, messages.SUCCESS,
                             ' Email has been sent to user Successfully')
            
            messages.add_message(request, messages.SUCCESS, "New Employee has been added!")
            return redirect('/admins/employee')
        else:
            messages.add_message(request, messages.ERROR, "Error")
            return redirect('/')
    dep = Department.objects.all()
    context = {
        'form': AddEmployee,
        'department':dep
    }
    return render(request, "admins/addEmployee.html", context)


@login_required
@admin_only
def deleteEmployee(request, employee_id):
    user = User.objects.get(id=employee_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS,
                         'Employee deleted successfully')
    return redirect('/admins/employee')

# ===================================================
# ======================= LEAVE =====================
# ===================================================

@login_required
def leaveManagement(request):
    leave=Leave.objects.all().order_by('-id')
    
    context = {
        'leaves': leave,
        'activate_leave': 'active bg-primary',
    }
    return render(request, 'admins/leaveManagement.html', context)


@login_required
def approveLeave(request, leave_id):
    leave = Leave.objects.get(id=leave_id)
    leave.status = 'Approved'
    leave.save()
    
    messages.add_message(request, messages.SUCCESS,
                        'Leave has been approved successfully')

    # if leave.status == 'Approved':
    #     template = render_to_string('admins/leaveApproved.html',
    #                                 {'name': request.user.username, 'leave': leave.leavetype})
    #     email = EmailMessage(
    #         'Thank You!!',
    #         template, settings.EMAIL_HOST_USER, ['samyakmanandhar2000@gmail.com'],
    #     )
    #     email.fail_silently = False
    #     print(request.user.email)
    #     email.send()
        
    #     messages.add_message(request, messages.SUCCESS,
    #                         ' Email has been sent to user Successfully')

    return redirect('/admins/leave_management')


def declineLeave(request, leave_id):
    order = Leave.objects.get(id=leave_id)
    order.status = 'Declined'
    order.save()
    messages.add_message(request, messages.SUCCESS,
                         'Leave has been declined !')
    return redirect('/admins/leave_management')
