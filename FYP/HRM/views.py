from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView
from .forms import ContactForm
from django.core.mail import mail_admins
from django.contrib import messages


def homepage(request):
    return render(request, "HRM/homepage.html")

# ===================================================
# ==================== ContactUs ================
# ===================================================


def contactUs(request):
        if request.method == 'POST':
            f = ContactForm(request.POST)

            if f.is_valid():
                name = f.cleaned_data['name']
                sender = f.cleaned_data['email']
                subject = "You have a new Message from {}:{}".format(name, sender)
                message = "Message: {}".format(f.cleaned_data['message'])
                mail_admins(subject, message)
                f.save()
                messages.add_message(request, messages.SUCCESS, 'Your Message Submitted Successfully.')
                return redirect('/contact-us')
            else:
                messages.add_message(request, messages.ERROR, 'Please recheck your feedback! ')


        else:
            f = ContactForm()

                
        return render(request, 'HRM/contactUs.html', {'form': f})