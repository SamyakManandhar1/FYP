from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.adminDashboard, name='admins'),


    path('department/', views.allDepartment, name='department' ),
    path('department_form', views.departmentForm, name='department_form'),
    path('delete_department/<int:department_id>', views.deleteDepartment, name='delete_department'),
    path('update_department/<int:department_id>', views.departmentUpdateForm, name='update_department'),

    path ('employee',views.employee, name='employee'),
    path ('add_employee',views.addEmployee, name='add_employee'),
    # path ('get_allorders',views.get_allorders, name='get_allorders'),



    path('alladmins/', views.allAdmins, name='alladmins' ),
    # path('demote_to_employee/<int:user_id>', views.demoteToEmployee, name='demote_to_employee'),

    # path('deactivate/<int:user_id>', views.deactivate, name='deactivate'),
    # path('reactivate/<int:user_id>', views.reactivate, name='reactivate'),

]