from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from Balance.models import *
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse


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
    name = ''
    email = ''
    comment = ''

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("first_name")
        email = form.cleaned_data.get("email_address")
        comment = form.cleaned_data.get("message")

        if request.user.is_authenticated():
            subject = str(request.user) + "'s Comment"
        else:
            subject ="A visitor's Comment"

        comment = name + "with the email," + email + ", sent the following message:\n\n" + comment;
        send_mail(subject, comment, 'dxtradeinvestment@gmail.com', [email])

        context = {'form':form}

        return render(request, 'contact.html', context)

    else:
        context = {'form':form}
        return render(request, "contact.html", context)

    
def investment(request):
	#return HttpResponse("about")
    return render(request, "investment.html")

@login_required 
def deposit(request):
	#return HttpResponse("about")
    message = request.POST.get('asset')
    subject = 'deposit'
    current_user =request.user
    user_email = current_user.email
    if message:
        if user.is_authenticated:
            try:
                send_mail(subject, message, user_email, ['dxtradeinvestment@gmail'])
            except BadHeaderError:
                return HttpResponse('Invalid header id')
        else:
            return HttpResponse('Please login')
    else:
        return render(request, "deposit.html")
       
