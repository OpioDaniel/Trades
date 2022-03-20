from django.db import models


class BizlandMainWeb(models.Model):
    company_name = models.CharField(max_length=20,  null=True)
    email = models.CharField(max_length=30,  null=True)
    contact = models.IntegerField(default='07')
    welcome_phrase = models.CharField(max_length=100,  null=True)
    welcome_phrase_description = models.CharField(max_length=500,  null=True)
    youtube_link = models.CharField(max_length=20,  null=True)
    main_image = models.ImageField(upload_to='biz', default='biz/unknown.png')

    about_title = models.CharField(max_length=500, null=True)
    about_description = models.CharField(max_length=20, null=True)
    about_image = models.ImageField(upload_to='biz', default='biz/unknown.png')
    about_title2 = models.CharField(max_length=100, null=True)
    about_description2 = models.CharField(max_length=500, null=True)
    about_description3 = models.CharField(max_length=500, null=True)


    def __str__(self):
        return self.company_name


class FeaturedServices(models.Model):
    company = models.ForeignKey(BizlandMainWeb, on_delete=models.CASCADE, related_name='fs')
    icon_name = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=500, null=True)


class AboutFL(models.Model):
    company = models.ForeignKey(BizlandMainWeb, on_delete=models.CASCADE, related_name='abfl')
    icon_name = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=500, null=True)
# Create your models here.
