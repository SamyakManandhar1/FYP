from django.urls import  path
from . import views


urlpatterns = [
    
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('reset-password-enterusername', views.entermailResetpassword,
         name='reset-password-enterusername'),
    path('reset-password/<token>/', views.resetPassword, name='reset-password'),
    path('reset-password-done', views.resetpasswordDone,
         name='reset-password-done'),
]