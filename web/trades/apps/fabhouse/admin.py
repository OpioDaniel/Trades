from django.contrib import admin
from .models import Page, PageInfo, CatalogCategorySections, CatalogCategorySectionsSub


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', )


@admin.register(PageInfo)
class PageInfoAdmin(admin.ModelAdmin):
    list_display = ('page', 'key', 'value')
    list_filter = ['page']


@admin.register(CatalogCategorySections)
class CatalogCategorySectionsAdmin(admin.ModelAdmin):
    list_display = ('page', 'section_id', 'section_name', 'section_description')
    list_filter = ['page']


@admin.register(CatalogCategorySectionsSub)
class CatalogCategorySectionsSubAdmin(admin.ModelAdmin):
    list_display = ('id', 'section_id', 'sub_id', 'data_date', 'left', 'data_caption', 'data_caption_link','Image' )
    list_filter = ['section']
    #
    # sub_id = models.CharField(max_length=10, null=True)
    # data_date = models.CharField(max_length=15, null=True)
    # left = models.SmallIntegerField(default=0)
    # Image = models.ImageField(upload_to='catalogs/')
    # data_caption = models.CharField(max_length=50, null=True)
    # data_caption_link = models.CharField(max_length=50, null=True)
