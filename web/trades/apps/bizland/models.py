from django.db import models
from django.urls import reverse


class Companies(models.Model):

    company_name = models.CharField(max_length=100, null=True)
    hero_image = models.ImageField(upload_to='hero/', default='main/unknown.png')
    logo_image = models.ImageField(upload_to='hero/', default='main/unknown.png')
    testimonial_background_image = models.ImageField(upload_to='testimonial/', default='main/unknown.png')
    contact_email_header = models.CharField(max_length=40, null=True)
    hero_title = models.CharField(max_length=100, null=True)
    hero_sub_title = models.CharField(max_length=100, null=True)
    hero_youtube_link = models.CharField(max_length=800, null=True)
    hero_description = models.CharField(max_length=500, null=True)
    hero_watch_title = models.CharField(max_length=100, null=True)
    address1 = models.CharField(max_length=100, null=True)
    address2 = models.CharField(max_length=100, null=True)
    address3 = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=True)
    faq_title = models.CharField(max_length=100, null=True)
    faq_description = models.CharField(max_length=500, null=True)
    pricing_title = models.CharField(max_length=100, null=True)
    pricing_description = models.CharField(max_length=500, null=True)
    service_title = models.CharField(max_length=100, null=True)
    service_description = models.CharField(max_length=500, null=True)
    team_title = models.CharField(max_length=100, null=True)
    team_description = models.CharField(max_length=500, null=True)
    about_image = models.ImageField(upload_to='about/', default='about/unknown.png')
    about_image1 = models.ImageField(upload_to='about/', default='about/unknown.png')
    about_title = models.CharField(max_length=100, null=True)
    about_description = models.CharField(max_length=500, null=True)
    about_header = models.CharField(max_length=100, null=True)
    about_header_description = models.CharField(max_length=500, null=True)
    about_description2 = models.CharField(max_length=500, null=True)
    portfolio_title = models.CharField(max_length=100, null=True)
    portfolio_description = models.CharField(max_length=500, null=True)
    contact_us_title = models.CharField(max_length=100, null=True)
    contact_us_description = models.CharField(max_length=500, null=True)
    subscribe_title = models.CharField(max_length=100, null=True)
    subscribe_description = models.CharField(max_length=500, null=True)
    Copyright_name = models.CharField(max_length=100, null=True)
    designer_name = models.CharField(max_length=500, null=True)
    designer_link = models.CharField(max_length=500, null=True)
    footer_links_title = models.CharField(max_length=100, null=True)
    footer_links_description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.company_name


class FAQ(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='faqs')
    title = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)


class Pricing(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='pricing')
    pricing_header = models.CharField(max_length=500, null=True)
    row_id = models.IntegerField(default=0)
    row1 = models.CharField(max_length=100, null=True)
    row2 = models.CharField(max_length=500, null=True)
    row3 = models.CharField(max_length=500, null=True)
    row4 = models.CharField(max_length=500, null=True)
    row5 = models.CharField(max_length=500, null=True)
    row6 = models.CharField(max_length=500, null=True)
    price_data_delay = models.IntegerField(default=0)
    number = models.IntegerField(null=True)

    def __str__(self):
        return self.pricing_header


class Service(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='service')
    icon_name = models.CharField(max_length=50, null=True)
    class_style = models.CharField(max_length=50, null=True)
    service_header = models.CharField(max_length=500, null=True)
    service_description = models.CharField(max_length=500, null=True)
    service_data_delay = models.IntegerField(default=0)


class Likeservice(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='l_service')
    icon_name = models.CharField(max_length=50, null=True)
    l_service_header = models.CharField(max_length=500, null=True)
    l_service_description = models.CharField(max_length=500, null=True)
    l_service_data_delay = models.IntegerField(default=0)


class Teams(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='team')
    team_id = models.IntegerField(default=0)
    Image = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=500, null=True)
    rank_title = models.CharField(max_length=500, null=True)
    team_data_delay = models.IntegerField(default=0)


class About(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='about')
    about_id = models.IntegerField(default=0)
    about_header1 = models.CharField(max_length=500, null=True)
    about_description1 = models.CharField(max_length=500, null=True)


class Testimonial(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='testimonial')
    testimonial_image = models.ImageField(upload_to='testimonial/', default='testimonial/unknown.png')
    testimonial_name = models.CharField(max_length=500, null=True)
    testimonial_rank = models.CharField(max_length=500, null=True)
    testimonial_description = models.CharField(max_length=500, null=True)


class Count(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='count')
    counts_title = models.CharField(max_length=50, null=True)
    class_style = models.CharField(max_length=50, null=True)
    icon_name = models.CharField(max_length=50, null=True)
    data_pure_counter_end = models.IntegerField(default=0)


class Client(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='client')
    client_image = models.ImageField(upload_to='client/', default='client/unknown.png')


class Skills(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='skill')
    skill_name = models.CharField(max_length=50, null=True)
    skill_counter = models.IntegerField(default=0)


class Contact(models.Model):

    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='contact')
    contact_us_title = models.CharField(max_length=50, null=True)
    contact_us_description = models.CharField(max_length=50, null=True)
    class_style = models.CharField(max_length=50, null=True)
    icon_name = models.CharField(max_length=50, null=True)


class ReceivedMessages(models.Model):
    class Meta:
        verbose_name = 'received_message'
        verbose_name_plural = 'received_messages'

    company = models.ForeignKey(Companies, null=True, on_delete=models.CASCADE, related_name='received_messages')
    name = models.CharField(max_length=100, default='', blank=True)
    email = models.CharField(max_length=100, default='', blank=True)
    subject = models.CharField(max_length=100, default='', blank=True)
    message = models.CharField(max_length=2000, default='', blank=True)


class PortfolioLi(models.Model):
    class Meta:
        ordering = ['id']

    company = models.ForeignKey(Companies, on_delete=models.CASCADE, related_name='portfolioli')
    li_port_name = models.CharField(max_length=50, null=True)
    li_port_name_capital = models.CharField(max_length=50, null=True)


class Portfolios(models.Model):

    class Meta:
        ordering = ['id']
    port_image = models.ImageField(upload_to='port/', default='port/unknown.png')
    port_name = models.CharField(max_length=50, null=True)
    port_name_capital = models.CharField(max_length=50, null=True)


