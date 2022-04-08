
from django.conf import settings
from django.urls import path, include

from django.urls import  include, path

urlpatterns = [
    path('',include('HRM.urls')),
    
    path('auth/',include('authentications.urls')),
    
    path('admins/',include('admins.urls')),
    
    path('employee/',include('employee.urls')),

]