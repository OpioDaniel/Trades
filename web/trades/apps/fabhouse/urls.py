from django.conf.urls import url
from .views import (home, catalog, about, contact, gallery)

app_name = "fabhouse"

urlpatterns = [

    url(r'catalog', catalog, name='catalog'),
    url(r'contact', contact, name='contact'),
    url(r'about', about, name='about'),
    url(r'gallery', gallery, name='gallery'),
    url(r'', home, name='home'),


]
