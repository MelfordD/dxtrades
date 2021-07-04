from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import balance
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

   
def wallet(request):
	#return HttpResponse("about")
    #valuenext=request.POST.get('next')
    user = balance.objects.all()
    return render(request, "wallet.html", {"user":user})
    
@login_required    
def deposit(request):
	#return HttpResponse("about")
    return render(request, "deposit.html")