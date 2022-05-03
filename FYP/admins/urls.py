from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.adminDashboard, name='dashboard'),


    path('department/', views.allDepartment, name='department'),
    path('department_form', views.departmentForm, name='department_form'),
    path('delete_department/<int:department_id>',
         views.deleteDepartment, name='delete_department'),
    path('update_department/<int:department_id>',
         views.departmentUpdateForm, name='update_department'),

    path('employee/', views.employee, name='employee'),
    path('add_employee', views.addEmployee, name='add_employee'),
    path('delete_employee/<int:employee_id>',
         views.deleteEmployee, name='delete_employee'),

    path('alladmins/', views.allAdmins, name='alladmins'),


    path('leave_management/', views.leaveManagement, name='leave_management'),
    path('approve_leave/<int:leave_id>',
         views.approveLeave, name='approve_leave'),
    path('decline_leave/<int:leave_id>',
         views.declineLeave, name='decline_leave'),


    path('attendance', views.attendance, name='attendance'),

    path('delete_attendance/<int:attendance_id>',
         views.deleteAttendance, name='delete_attendance'),
    
    
    path('all-messages', views.allContact, name='all-messages'),




]
