from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import *

admin.site.register(Reception)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Order)


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['email', 'username',]


admin.site.register(User, UserAdmin)

# Register your models here.
