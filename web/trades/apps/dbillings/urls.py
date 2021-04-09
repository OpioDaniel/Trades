from django.conf.urls import url
from .views import (index, customers, create_customer, CustomerDetail)

app_name = "dbillings"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^Customers$', customers, name='list_Customer'),
    url(r'^create_customer$', create_customer, name='create_customer'),
    url(r'Customers/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='detailed_customer'),
]
