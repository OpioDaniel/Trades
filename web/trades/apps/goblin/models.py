from django.db import models


class Citizen(models.Model):
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField()
    origin = models.CharField(max_length=20, blank=True, null=True)
# Create your models here.
