from django.db import models


class Apes(models.Model):
    logo_image = models.ImageField(upload_to='apewives', default='apewives/unknown.png')
    apewives_title = models.CharField(max_length=20, default='')
    apewives_image = models.ImageField(upload_to='apewives', default='apewives/unknown.png')
    about_the_apewives = models.CharField(max_length=50, default='')
    about_the_apewives_description = models.CharField(max_length=500, default='')


class SlidingTitle(models.Model):
    description = models.CharField(max_length=50, default='')


class SlidingImages(models.Model):
    sliding_images = models.ImageField(upload_to='apewives', default='apewives/unknown.png')


class Trial(models.Model):
    image = models.ImageField(upload_to='apewives/images/', default='apewives/unknown.png')