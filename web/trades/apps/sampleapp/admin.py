from django.contrib import admin
from .models import TeamMembers


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'image']
