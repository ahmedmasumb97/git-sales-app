from django.contrib import admin
from .models import Profile,UserOTP
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdminUser


# Register your models here.


class profileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'



class UserOTPInline(admin.StackedInline):
    model = UserOTP
    can_delete = False
    verbose_name_plural = 'User otp'



class userAdmin(BaseAdminUser):
    inlines = [profileInline,UserOTPInline]


# unregister your previously user

admin.site.unregister(User)
admin.site.register(User,userAdmin)