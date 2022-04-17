from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
# from .forms import *
# Create your views here.


# class EmployeeRegistrationView(CreateView):
    # template_name = "emoployeeregistration.html"
    # form_class =  EmployeeRegistrationForm
    # success_url = reverse_lazy("HRM:home")
    
    # def form_valid(self, form):
    #     username = form.cleaned_data.get("username")
    #     password = form.cleaned_data.get("password")
    #     email = form.cleaned_data.get("email")
    #     user=User.objects.create_user(username=username, email=email, password=password)
    #     form.instance.user=user
    #     # login(self.request, user)
    #     return super().form_valid(form)


def homepage(request):
    return render(request, "HRM/homepage.html")

def about(request):
    return render(request, "HRM/aboutus.html")    