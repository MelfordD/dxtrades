from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from Balance.models import *
from django.contrib.auth.models import User
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
                'first_name': form.cleaned_data['first_name'], 
                'last_name': form.cleaned_data['last_name'], 
                'email': form.cleaned_data['email_address'], 
            }
            message = "\n".join(body.values()), form.cleaned_data['message'] 
        try:
            send_mail(subject, message, 'dxtradeinvestment@gmail.com', ['dxtradeinvestment@gmail.com']) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect ('home')
    form = ContactForm() 
    return render(request, "contact.html", {'form':form})

    
def investment(request):
	#return HttpResponse("about")
    return render(request, "investment.html")

@login_required 
def deposit(request):
	#return HttpResponse("about")
    if request.method == 'POST':
        account = request.POST.get('asset')
        balance = Balance()
        balance.asset = balance
        balance.save()
        return render(request, "deposit.html")
    else:
        return render(request, "deposit.html")
       
