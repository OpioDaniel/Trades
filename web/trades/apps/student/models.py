from django.db import models


class Students(models.Model):
    full_name = models.CharField(max_length=20, null=True, blank=False)
    country = models.CharField(max_length=20, null=True, blank=False)
# Create your models here.
