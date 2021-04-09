from django.contrib import admin

from .models import GamePlatform, Game, PriceList, ShoppingCart

admin.autodiscover()

admin.site.register(GamePlatform)
admin.site.register(Game)
admin.site.register(PriceList)
admin.site.register(ShoppingCart)
