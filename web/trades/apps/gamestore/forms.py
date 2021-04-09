from django import forms
from django.forms import inlineformset_factory
from .models import ShoppingCartItem
from .models import ShoppingCart


ShoppingCartFormSet = inlineformset_factory(
  ShoppingCart,
  ShoppingCartItem,
  fields=('quantity', 'price_per_unit'),
  extra=0,
  widgets={
      'quantity': forms.TextInput({
         'class': 'form-control quantity',
      }),
      'price_per_unit': forms.HiddenInput()
  }
)
