from django.conf.urls import url
from .views import index, post_contact_us

app_name = "bizland"

urlpatterns = [
    url(r'^$', index, name='index'),
    url('^post_contact_us$', post_contact_us, name='post_contact_us'),
]
