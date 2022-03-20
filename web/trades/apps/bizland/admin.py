from django.contrib import admin
from .models import (Companies, FAQ, Pricing, Service, Likeservice, Teams, About, Testimonial, Count, Client, Skills,
                     Contact, ReceivedMessages, Portfolios, PortfolioLi)


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone', )


@admin.register(FAQ)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'title', )


@admin.register(Pricing)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'pricing_header', 'row_id', 'price_data_delay')


@admin.register(Service)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'service_header', 'class_style', 'icon_name')


@admin.register(Likeservice)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'l_service_header', 'icon_name',)


@admin.register(Teams)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'name', 'rank_title', 'team_id', 'team_data_delay')


@admin.register(About)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'about_header1', 'about_id')


@admin.register(Testimonial)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'testimonial_name', 'testimonial_rank')


@admin.register(Count)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'counts_title', 'class_style', 'icon_name')


@admin.register(Client)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'client_image')


@admin.register(Skills)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'skill_name', 'skill_counter')


@admin.register(Contact)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('company', 'contact_us_title', 'class_style', 'icon_name', 'contact_us_description')


@admin.register(ReceivedMessages)
class ReceivedMessagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message',)


@admin.register(Portfolios)
class PortfoliosAdmin(admin.ModelAdmin):
    list_display = ('port_name', 'port_name_capital', )


@admin.register(PortfolioLi)
class PortfolioLiAdmin(admin.ModelAdmin):
    list_display = ('li_port_name', 'li_port_name_capital', )
