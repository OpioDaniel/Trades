from django.conf.urls import url
from .views import index, show_highlighted_games, show_all_games, ShoppingCartEditView, add_to_cart

app_name = "gamestore"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^games-list/highlighted$', show_highlighted_games, name='gameshighlighted'),
    url(r'^games-list/all$', show_all_games, name='gamesall'),
    url(r'^cart$', ShoppingCartEditView.as_view(), name='user-cart'),
    url(r'cart/add/(?P<game_id>\d+)$', add_to_cart, name='cart'),
]
