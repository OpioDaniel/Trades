from django.db import models


class Source(models.Model):
    type = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.type


class Product(models.Model):
    sitc2 = models.SmallIntegerField(default=0, blank=True)
    description = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return str(self.sitc2) + ' ' + str(self.description)


class YearData(models.Model):
    source = models.ForeignKey(Source, null=True, on_delete=models.CASCADE, related_name='source_year_data')
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='product_year_data')
    year = models.SmallIntegerField(default=0, null=False, blank=False)
    value = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return 'source: ' + str(self.source.id) + ' product: ' + str(self.product.id) + ' ' + str(self.year) + ' ' + str(self.value)

# class Charts(models.Model):
