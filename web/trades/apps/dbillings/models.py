from django.db import models
from django.urls import reverse


class Customer(models.Model):
    customer_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        return reverse('dbillings:detailed_customer', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Invoice(models.Model):
    invoice_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.last_name + ': ' + str(self.invoice_number)


class Item(models.Model):
    item_number = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.item_name


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(max_digits=11, decimal_places=2, default=0)
