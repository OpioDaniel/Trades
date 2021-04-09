from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm
from .models import (GlobUser, UserProfile)


admin.site.register(UserProfile)


class GlobUserAdmin(UserAdmin):
    add_form = RegistrationForm
    model = GlobUser
    list_display = ['email', 'username', ]


admin.site.register(get_user_model(), GlobUserAdmin)
