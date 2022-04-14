from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.employeeDashboard, name='dashboard'),
    
    
    path('employeeprofile',views.employeeProfile, name='employeeprofile'),

    path('employee_update_profile', views.employeeUpdateProfile,
         name='employee_update_profile'),
    
    
    path('leave',views.leave, name='leave'),
    path('attendance', views.attendance, name='attendance'),


    

]