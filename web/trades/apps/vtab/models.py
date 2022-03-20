from django.db import models


class EquipmentMain(models.Model):
    title1 = models.CharField(max_length=50, blank=True)
    title2 = models.CharField(max_length=50, blank=True)
    title3 = models.CharField(max_length=50, blank=True)


class Equipments1(models.Model):
    img1 = models.ImageField(upload_to='equipment', default='equipment/unknown.png')


class Equipments2(models.Model):
    img2 = models.ImageField(upload_to='equipment', default='equipment/unknown.png')


class Equipments3(models.Model):
    img3 = models.ImageField(upload_to='equipment', default='equipment/unknown.png')


class Tabs(models.Model):
    atm_name = models.CharField(max_length=50, blank=True)
    tab_name = models.CharField(max_length=50, blank=True)
    tab_text = models.TextField(blank=True)
    tab_text_function = models.TextField(blank=True)

    def __str__(self):
        return str(self.tab_name) + ":" + str(self.tab_name)