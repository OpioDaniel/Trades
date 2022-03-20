from django.db import models


class Citizen(models.Model):
    full_name = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)













# Create your models here.
