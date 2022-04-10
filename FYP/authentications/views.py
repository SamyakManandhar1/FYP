from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.shortcuts import redirect, render
from multiprocessing import context
from django.contrib.auth import authenticate,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import CreateUserForm
from django.contrib import auth

from authentications.auth import unauthenticated_user, employee_only
from django.contrib.auth.decorators import login_required
# from .models import Profile
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# Create your views here.

@employee_only
def signup(request):
    if request.method=='POST':
        userdata = CreateUserForm(request.POST)
        if userdata.is_valid():
            user=userdata.save()
            user.save()
            # Profile.objects.create(user=user, username=user.username, email= user.email) 

            messages.add_message(request, messages.SUCCESS, f'{user.username} successfully registered to HRM.' )
            return redirect('/')
        else:
            context = {'form' : userdata}
            messages.add_message(request, messages.ERROR, 'Unable to register User!' )
            return render(request, 'authentications/signup.html',context)


    context ={
            'form' : CreateUserForm,
            'activate_register': 'active',
    }
    return render(request, 'authentications/signup.html', context)


@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if user.is_superuser and user.is_staff and user.is_active:
                return redirect('/admins/dashboard')
            else:
                return redirect('/employee/dashboard')
        else:
            messages.error(request, "Username or Password is incorrect.")
            return render(request, 'authentications/login.html',{})
    context={
            'activate_login': 'active',
    }
    return render(request, 'authentications/login.html',context)

@login_required
def signout(request):
    logout(request)
    return redirect('/')