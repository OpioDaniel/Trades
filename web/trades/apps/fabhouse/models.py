from django.db import models
from django.urls import reverse


class Page(models.Model):
    page_name = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.page_name

class PageInfo(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_infos')
    key = models.CharField(max_length=50, null=True)
    value = models.CharField(max_length=1020, null=True)

class CatalogCategorySections(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='catalog_category_sections')
    section_id = models.CharField(max_length=50, null=True)
    section_name = models.CharField(max_length=50, null=True)
    section_description = models.CharField(max_length=1020, null=True)

    def __str__(self):
        return self.section_name

class CatalogCategorySectionsSub(models.Model):
    section = models.ForeignKey(CatalogCategorySections,
                                on_delete=models.CASCADE, related_name='catalog_category_sections_sub')

    sub_id = models.CharField(max_length=10, null=True)
    data_date = models.CharField(max_length=15, null=True)
    left = models.SmallIntegerField(default=0)
    Image = models.ImageField(upload_to='catalogs/')
    data_caption = models.CharField(max_length=50, null=True)
    data_caption_link = models.CharField(max_length=50, null=True)

    def get_absolute_url(self):
        return reverse('fabhouse:catalog_image', kwargs={'pk': self.pk})

    def __str__(self):
        return self.data_caption + ' ' + str(self.Image)


class CatalogCategorySectionsSubTitle(models.Model):
    sub_section = models.ForeignKey(CatalogCategorySectionsSub,
                                    on_delete=models.CASCADE, related_name='sections_sub_title')
    title = models.CharField(max_length=250, null=True)


class TitleImages(models.Model):
    sub_title = models.ForeignKey(CatalogCategorySectionsSubTitle,
                                    on_delete=models.CASCADE, related_name='sub_titles')
    image_title = models.CharField(max_length=250, null=True)
    Image = models.ImageField(upload_to='catalogs/title/')


class PageGallery(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='page_gallery')
    id_number = models.SmallIntegerField(default=0)
