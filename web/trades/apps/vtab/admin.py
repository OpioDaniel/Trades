from django.contrib import admin
from .models import Equipments1, Equipments2, Equipments3, EquipmentMain, Tabs


@admin.register(Tabs)
class TabsAdmin(admin.ModelAdmin):
    list_display = ('tab_name', )


@admin.register(EquipmentMain)
class EquipmentMainAdmin(admin.ModelAdmin):
    list_display = ('title1', 'title2', 'title3', )


@admin.register(Equipments1)
class Equipments1Admin(admin.ModelAdmin):
    list_display = ('img1', )


@admin.register(Equipments2)
class Equipments2Admin(admin.ModelAdmin):
    list_display = ('img2', )


@admin.register(Equipments3)
class Equipments3Admin(admin.ModelAdmin):
    list_display = ('img3', )