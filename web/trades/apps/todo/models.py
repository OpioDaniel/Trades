from django.db import models


class Item(models.Model):
    text = models.TextField(blank=False, null=False)
    date_posted = models.DateField(auto_now=True)


class TeamMembers(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='shoes/', default='shoes/unknown.png')

