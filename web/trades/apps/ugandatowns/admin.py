from django.contrib import admin
from .models import Towns


@admin.register(Towns)
class TownsAdmin(admin.ModelAdmin):
    list_display = ['town_name', 'town_clerk_full_name', 'address', 'image', 'order']
