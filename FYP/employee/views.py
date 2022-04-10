from django.shortcuts import render

# from FYP.authentications.auth import employee_only
# from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
# @employee_only
def employeeDashboard(request):
    return render(request, "employee/employeeDashboard.html")