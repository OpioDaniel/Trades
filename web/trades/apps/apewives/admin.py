from django.contrib import admin
from .models import Apes, SlidingTitle, SlidingImages, Trial

@admin.register(Apes)
class ApesAdmin(admin.ModelAdmin):
    list_display = ('apewives_title',)


@admin.register(SlidingTitle)
class SlidingTitleAdmin(admin.ModelAdmin):
    list_display = ('description', )


@admin.register(SlidingImages)
class SlidingImagesAdmin(admin.ModelAdmin):
    list_display = ('sliding_images',)


@admin.register(Trial)
class TrialAdmin(admin.ModelAdmin):
    list_display = ('image',)
