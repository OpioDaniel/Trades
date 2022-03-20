from django.conf.urls import url
from .views import index,detailed_town

app_name = "ugandatowns"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'uganda_towns/(?P<pk>\d+)/$', detailed_town, name='detailed_town'),

]
