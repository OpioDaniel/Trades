from django.contrib import admin
from .models import Citizen


@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')

# Register your models here.
