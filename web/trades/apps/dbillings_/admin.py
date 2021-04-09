from django.contrib import admin
from .models import Customer, Item, Invoice, InvoiceItem


@admin.register(Customer)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ('customer_number', 'first_name', 'last_name')


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer', 'invoice_date')


@admin.register(InvoiceItem)
class InvoicesItemsAdmin(admin.ModelAdmin):
    list_display = ('invoice', 'item', 'quantity', 'unit_price')

@admin.register(Item)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('item_number', 'item_name')

