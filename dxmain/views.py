from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from Balance.models import *
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.conf import settings


# Create your views here.


def home(request):
	#return HttpResponse("about")
    return render(request, "index.html")
    
def about(request):
	#return HttpResponse("about")
    return render(request, "about.html")
    
def services(request):
	#return HttpResponse("about")
    return render(request, "services.html")    
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        main = str(message)
        
        send_mail('Contact Form from ' + str(name), main, email, ['dxtradeinvestment@gmail'], fail_silently=False)
        
    return render(request, "contact.html")

    
def investment(request):
	#return HttpResponse("about")
    return render(request, "investment.html")

@login_required 
def deposit(request):
    if request.method == 'POST':
        amount = request.POST.get('asset')
        current_user =request.user
        message = 'I want to deposit ' + str(amount) + ' from ' + str(current_user)
        
        send_mail('Deposit', message, settings.EMAIL_HOST_USER, ['dxtradeinvestment@gmail'], fail_silently=False)
        
    return render(request, "deposit.html")
       
