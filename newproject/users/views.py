from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.contrib.auth import logout as authlogout
from django.contrib.auth import authenticate,login as authlogin
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required



# Create your views here.


@never_cache
def signup(request):
    user=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(username=username,password=password)                      
    return render(request,'users/signup.html',{'user':user})

@never_cache
def login(request):
        error=None
        if request.POST:
            username=request.POST['username']
            password=request.POST['password']  
            user=authenticate(username=username,password=password)
            if user:
                authlogin(request,user)
                return redirect('home')  
            else:
                 error='invalid credentials' 
        return render(request,'users/login.html',{'error':error})


@never_cache
@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'users/home.html', context)

def logout(request):
    authlogout(request)
    return redirect ('login')
