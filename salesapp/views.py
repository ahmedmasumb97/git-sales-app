from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile,UserOTP
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import random

# Create your views here.

def login_view(request):

    
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home page if user is already logged in.
    
    if request.method == "POST":
        form = LoginForm(request.POST,data =request.POST)
        if form.is_valid():
            user =  form.get_user()
            otp = ''.join([str(random.randint(0,6)) for i in range(6)])
            user_otp,created = UserOTP.objects.get_or_create(user=user)
            user_otp.otp = otp
            user_otp.save()
            request.session['pre_otp_user_id'] = user.id
            return redirect('otp')
            
            
            
            # if User is None:
            #     return redirect('login')
            # login(request,user)
            # return redirect('home')
    
    form = LoginForm()
    return render(request,'login.html',{'form':form})


@login_required
def home_view(request):
    return render(request,'home.html')
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


# otp

def otp_view(request):
    form = UserOTP()
    return render(request,'otp.html',{'form':form})












#templates


def template(request):
    return render(request,'index.html')