from django.shortcuts import render

# Create your views here.


def employeeDashboard(request):
    return render(request, "employee/employeeDashboard.html")