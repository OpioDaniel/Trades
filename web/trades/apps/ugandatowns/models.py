from django.db import models


class Towns(models.Model):
    class Meta:
        ordering = ['order']

    town_name = models.CharField(max_length=50, blank=False, null=False)
    town_clerk_full_name = models.CharField(max_length=50, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(upload_to='ugandatowns/', default='ugandatowns/unknown.png')
    order = models.SmallIntegerField(default=0)

    # def get_absolute_url(self):
    #     return reverse('ugandatowns:detailed_town', kwargs={'pk': self.pk})

    def __str__(self):
        return self.town_name

