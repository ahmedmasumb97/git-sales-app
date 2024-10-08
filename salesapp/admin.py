from django.contrib import admin
from .models import Profile,UserOTP
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseAdminUser  


# Register your models here.

#profileInline: This class defines how the Profile model will be displayed alongside the User model in the Django admin.
class profileInline(admin.StackedInline):
    model = Profile#: This connects the Profile model to the inline form.
    can_delete = False #This prevents the Profile from being deleted from the User page.
    verbose_name_plural = 'Profile' # Sets a human-readable plural name for the admin interface.




class UserOTPInline(admin.StackedInline):#admin.StackedInline: This allows you to display the related Profile model as a "stacked" section in the admin form for the User model.
    model = UserOTP
    can_delete = False
    verbose_name_plural = 'User otp'


# add those classes in admin panel
class userAdmin(BaseAdminUser): #: A custom admin class that extends the default BaseAdminUser class.
    inlines = [profileInline,UserOTPInline] #his adds both Profile and UserOTP models as inline sections in the User model’s admin form, allowing you to view and edit the related Profile and UserOTP information directly on the user page.
    
    # question is:  why user baseModelUser instead of UserAdmin
    
    # answer:
    # UserAdmin is a built-in Django admin class that provides basic user management functionality, while UserBaseAdminUser is a custom admin class that extends the default Django User model, allowing you to add custom fields and methods to the User model. By using UserBaseAdminUser, you can add the custom fields and methods to the User model without losing the default functionality provided by UserAdmin.
    # Note: The UserBaseAdminUser class is not available in Django 4.0 and above. If you are using Django 4.0 or above, you should use UserAdmin instead of UserBaseAdminUser.
    #removing naming conflicts between custome class(BaseAdminUser) and main class(UserAdmin)
    #  Clear Separation of Default vs Custom Logic:
    #3. Customization Flexibility:
    # Using a separate class name allows you to add customizations to the UserAdmin without affecting the default behavior of Django’s original UserAdmin. It’s a good practice to keep the original class separate from your modifications so that you can always refer to the base functionality if needed.
    
    
#  BaseUserAdmin is just an alias for UserAdmin. It reflects the same functionality as the main class (UserAdmin) and is often used to avoid naming conflicts or to make the code more readable.
# The behavior remains the same, so any customizations you make to a class extending BaseUserAdmin will apply to the original UserAdmin functionality.


# unregister your previously user

admin.site.unregister(User) #This removes the default User model from the admin site.
admin.site.register(User,userAdmin)# This registers your custom userAdmin class, which now includes the Profile and UserOTP inlines, effectively overriding the default admin panel for the User model.