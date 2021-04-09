from django.contrib import admin
from .models import Item, TeamMembers


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['text']


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'image']
