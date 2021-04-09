from django.db import models
from django.conf import settings
from django.db.models import Count


class GamePlatform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GameManager(models.Manager):
    def get_highlighted(self):
        return self.filter(highlighted=True)

    def get_not_highlighted(self):
        return self.filter(highlighted=False)

    def get_by_platform(self, platform):
        return self.filter(gameplatform__name__iexact=platform)


class Game(models.Model):
    class Meta:
        ordering = ['-highlighted', 'name']

    name = models.CharField(max_length=100)
    release_year = models.IntegerField(null=True)
    developer = models.CharField(max_length=100)
    published_by = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gamestore/', default='gamestore/placeholder.png', max_length=100)
    gameplatform = models.ForeignKey(GamePlatform, null=False, on_delete=models.CASCADE)
    highlighted = models.BooleanField(default=False)

    objects = GameManager()

    def __str__(self):
        return self.gameplatform.name + ' ' + self.name


class PriceList(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    price_per_unit = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.game.name


class ShoppingCartManager(models.Manager):

    def get_by_id(self, id):
        return self.get(pk=id)

    def get_by_user(self, user):
        try:
            u = self.get(user_id=user.id)
        except ShoppingCart.DoesNotExist:
            u = self.create(user=user)
        return u

    def create_cart(self, user):
        new_cart = self.create(user=user)
        return new_cart

    def get_last_by_user(self, user):
        max_bill = self.filter(user_id=user.id).aggregate(max_bill=Count('id'))['max_bill']
        return self.get(id=max_bill)


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, on_delete=models.CASCADE)
    objects = ShoppingCartManager()

    def __str__(self):
        return self.user.username + '\'s shopping cart'


class ShoppingCartItemManager(models.Manager):

    def get_items(self, cart):
        return self.filter(cart_id=cart.id)

    def get_existing_item(self, cart, game):
        try:
            return self.get(cart_id=cart.id,
                            game_id=game.id)
        except ShoppingCartItem.DoesNotExist:
            return None


class ShoppingCartItem(models.Model):
    quantity = models.IntegerField(null=False)
    price_per_unit = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    cart = models.ForeignKey(ShoppingCart, null=False, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE, related_name='items')

    objects = ShoppingCartItemManager()
