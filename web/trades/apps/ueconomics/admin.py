from django.contrib import admin
from .models import Source, Product, YearData


class SourceAdmin(admin.ModelAdmin):
    list_display = ['type']
    list_filter = ['type']


admin.site.register(Source, SourceAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['sitc2', 'description']


admin.site.register(Product, ProductAdmin)


class YearDataAdmin(admin.ModelAdmin):
    list_display = ['source', 'product', 'year', 'value']
    list_filter = ['source', 'product']


admin.site.register(YearData, YearDataAdmin)

