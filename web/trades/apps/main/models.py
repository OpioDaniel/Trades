from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class GlobUser(AbstractUser):
    pass


# Users
class UserProfile(models.Model):
    TYPES = (
        (0, 'Staff'),
        (1, 'Student'),
        (2, 'Instructor'),
    )
    user = models.OneToOneField(GlobUser, on_delete=models.CASCADE, primary_key=True)
    description = models.CharField(max_length=100, default='', blank=True)
    city = models.CharField(max_length=100, default='', blank=True)
    country = models.CharField(max_length=100, default='', blank=True)
    website = models.URLField(default='http://JerusalemCollege.org', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    type = models.IntegerField(default=1, choices=TYPES)
    image = models.ImageField(upload_to='main/', default='main/unknown.png')

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


# Registrations
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        user_profile.save()


post_save.connect(create_profile, sender=GlobUser)

