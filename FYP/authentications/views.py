from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib import auth
from authentications.auth import unauthenticated_user
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .auth import unauthenticated_user
from django.contrib.auth.decorators import login_required
from admins.models import Profile
from django.core.mail import send_mail
from django.conf import settings
import uuid


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
            return render(request, 'authentications/login.html')

    return render(request, 'authentications/login.html')


@login_required
def signout(request):
    logout(request)
    return redirect('/')


def send_forget_password_mail(email, token):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://localhost:8000/auth/reset-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


def entermailResetpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # .first()) checks if the user exists
        if not User.objects.filter(username=username).first():
            messages.add_message(request, messages.ERROR,
                                 f'No user found with {username} username.')
            return redirect('/auth/reset-password-enterusername')

        user_obj = User.objects.get(username=username)
        # Generating random token and converting to string
        token = str(uuid.uuid4())

        # Fetching user profile data
        profile_obj = Profile.objects.get(user=user_obj)
        # Saving token in user profile
        profile_obj.forget_password_token = token
        # Saving user profile
        profile_obj.save()

        # Sending mail to user with link and token
        send_forget_password_mail(user_obj.email, token)
        # Showing message to user
        messages.add_message(request, messages.SUCCESS,
                             'An email is sent to user with password changing link.')
        return redirect('/auth/reset-password-enterusername')

    return render(request, 'authentications/reset-password-enterusername.html')


def resetPassword(request, token):
    profile_obj = Profile.objects.filter(forget_password_token=token).first()
    context = {'user_id': profile_obj.user.id}

    if request.method == 'POST':

        new_password = request.POST.get('password-1')
        confirm_new_password = request.POST.get('password-2')
        user_id = request.POST.get('user_id')

        if new_password != confirm_new_password:
            messages.add_message(request, messages.ERROR,
                                 'Password must be same.')
            return redirect(f'/auth/reset-password/{token}/')

        # Matching user with user id
        user_obj = User.objects.get(id=user_id)
        # Updating password
        user_obj.set_password(new_password)
        # Saving user password
        user_obj.save()

        return render(request, 'authentications/reset-password-done.html')

    return render(request, 'authentications/reset-password.html', context)


def resetpasswordDone(request):
    messages.add_message(request, messages.SUCCESS, 'Password reset')
    return render(request, 'authentications/reset-password-done.html')
