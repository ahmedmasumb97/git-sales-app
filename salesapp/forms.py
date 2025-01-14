from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'password'}))
    



class OtpForm(forms.Form):
    otp = forms.CharField(max_length=6,widget = forms.TextInput(attrs={'placeholder':'OTP'}))