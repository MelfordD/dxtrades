from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *



# Create your views here.


def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('wallet')
        else:
            messages.info(request, "Invalid Credentials")
    else:
        return render(request, "login.html")
    
    



def signup(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        
        
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,  password=password, first_name=first_name, last_name=last_name, email=email,)
                user.save();
                print('user created')
        else:
            messages.info(request, "Password doen't match")
            return redirect('signup')
        return redirect('/')
        
    else:    
        return render(request, "signup.html")
       
    

def logout(request):
    auth.logout(request)
    return redirect('/')
    
