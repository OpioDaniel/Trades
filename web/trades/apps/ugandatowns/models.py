from django.db import models
from django.shortcuts import reverse

class Towns (models.Model):
    class Meta:
        ordering = ['order']
    town_name = models.CharField(max_length=100,blank=False)
    town_clerk_fullname = models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=100,blank=False)
    address = models.CharField(max_length=100,blank=False)
    order = models.SmallIntegerField(default=0)
    Image = models.ImageField(upload_to='ugandatowns/')

    def get_absolute_url(self):
        return reverse('ugandatowns:detailed_town', kwargs={'pk': self.pk})

    def __str__(self):
        return self.town_clerk_fullname + ' ' + self.town_name + ' ' + self.email + '' + str(self.order)


# Create your models here.
