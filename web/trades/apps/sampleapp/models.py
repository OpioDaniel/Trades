from django.db import models


class TeamMembers(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='sampleapp/', default='sampleapp/unknown.png')

# Create your models here.
