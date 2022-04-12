from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.adminDashboard, name='admins'),


    path('department/', views.allDepartment, name='department' ),
    path('department_form', views.departmentForm, name='department_form'),
    path('delete_department/<int:department_id>', views.deleteDepartment, name='delete_department'),
    path('update_department/<int:department_id>', views.departmentUpdateForm, name='update_department'),

    # path ('get_feedback',views.get_feedback, name='get_feedback'),
    # path ('get_allservices',views.get_allservices, name='get_allservices'),
    # path ('get_allorders',views.get_allorders, name='get_allorders'),



    path('alladmins/', views.allAdmins, name='alladmins' ),
    # path('demote_to_employee/<int:user_id>', views.demoteToEmployee, name='demote_to_employee'),

    # path('deactivate/<int:user_id>', views.deactivate, name='deactivate'),
    # path('reactivate/<int:user_id>', views.reactivate, name='reactivate'),

]