from django.conf.urls import url
from .views import index

app_name = "sampleapp"

urlpatterns = [
    url(r'^$', index, name='index'),

]
