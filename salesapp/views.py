from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,UserOTP
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST,data =request.POST)
        if form.is_valid():
            user =  form.get_user()
            if User is None:
                return redirect('login')
            login(request,user)
            return redirect('home')
    
    form = LoginForm()
    return render(request,'login.html',{'form':form})



def home_view(request):
    return render(request,'home.html')