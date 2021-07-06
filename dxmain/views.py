from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User


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
	#return HttpResponse("about")
    return render(request, "contact.html")
    
def investment(request):
	#return HttpResponse("about")
    return render(request, "investment.html")

   

    
@login_required    
def deposit(request):
	#return HttpResponse("about")
    return render(request, "deposit.html")