
from django.urls import path
from .views import login_view,home_view,logout_view,otp_view,template

urlpatterns = [
      path('login/', login_view, name='login'),
      path('home/', home_view, name='home'),
      path('logout/',logout_view, name='logout'),  
      path('otp/',otp_view, name='otp'),
      path('template/',template,name='template')
]

