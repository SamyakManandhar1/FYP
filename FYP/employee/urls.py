from django.urls import path
from . import views

urlpatterns = [
    path('dashboard',views.employeeDashboard, name='dashboard'),
    
    
    # path('customerprofile',views.customerProfile, name='customerprofile'),
    # path('customerupdateprofile',views.customerUpdateProfile, name='customerupdateprofile'),
    # path('my_bookings',views.myBookings, name='my_bookings'),
    # path ('feedback_form/<int:service_id>',views.feedbackForm, name='feedback_form'),


    

]