from django.contrib import admin
from .models import Towns



class TownsAdmin(admin.ModelAdmin):
    list_display = ['town_clerk_fullname' , 'town_name' , 'email','order']

admin.site.register(Towns, TownsAdmin)

# Register your models here.
