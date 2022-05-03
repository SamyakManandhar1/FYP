from django.urls import  path
from . import views


urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('contact-us', views.contactUs, name='contact-us'),

]
