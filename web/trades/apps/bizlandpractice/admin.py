from django.contrib import admin
from .models import BizlandMainWeb, FeaturedServices,AboutFL


@admin.register(BizlandMainWeb)
class BizlandMainWebAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email',)


@admin.register(FeaturedServices)
class FeaturedServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AboutFL)
class AboutFLAdmin(admin.ModelAdmin):
    list_display = ('title',)