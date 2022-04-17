import imp
from tabnanny import verbose
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm
#     form = UserChangeForm
#     modal = CustomUser
#     list_display = (
#         'username', 'email', 'first_name', 'last_name', 'is_staff'
#         )
#     add_fieldsets = UserAdmin.add_fieldsets+(
#         (None,{"fields":("email","first_name","last_name", "is_student")}))
#     fieldsets = UserAdmin.add_fieldsets+((None,{"fields":("email","first_name","last_name", "is_student")}))

    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password')
    #     }),
    #     ('Personal info', {
    #         'fields': ('first_name', 'last_name', 'email')
    #     }),
    #     ('Permissions', {
    #         'fields': (
    #             'is_active', 'is_staff', 'is_superuser',
    #             'groups', 'user_permissions'
    #             )
    #     }),
    #     ('Important dates', {
    #         'fields': ('last_login', 'date_joined')
    #     }),
    #     ('Additional info', {
    #         'fields': ('is_student', 'is_teacher', 'mailing_address')
    #     })
    # )

    # add_fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password1', 'password2')
    #     }),
    #     ('Personal info', {
    #         'fields': ('first_name', 'last_name', 'email')
    #     }),
    #     ('Permissions', {
    #         'fields': (
    #             'is_active', 'is_staff', 'is_superuser',
    #             'groups', 'user_permissions'
    #             )
    #     }),
    #     ('Important dates', {
    #         'fields': ('last_login', 'date_joined')
    #     }),
    #     ('Additional info', {
    #         'fields': ('is_student',)
    #     })
    # )

# admin.site.register(CustomUser, CustomUserAdmin)

from .models import CustomUser

class DepartmentInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "Department"

class CustomUserAdmin (UserAdmin):
    inlines = (DepartmentInline,)
admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)
