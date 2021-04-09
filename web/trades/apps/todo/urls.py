from django.conf.urls import url
from .views import (index, draw, member)

app_name = "todo"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^member/(?P<pk>\d+)/$', member, name='member'),
    url(r'^draw$', draw, name='draw'),
]
