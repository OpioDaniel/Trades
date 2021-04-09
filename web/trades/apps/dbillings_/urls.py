from django.conf.urls import url
from .views import (index,
                    customers,
                    # CustomersView,
                    CustomerDetail,
                    # CreateCustomer,
                    create_customer,
                    UpdateCustomer, DeleteCustomer)

app_name = "dbillings"

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^Customers$', customers, name='list_Customer'),
    # url(r'^Customers$', CustomersView.as_view(), name='list_Customer'),
    # url(r'^CreateCustomers/$', CreateCustomer.as_view(), name='create_customer'),
    url(r'^CreateCustomers/$', create_customer, name='create_customer'),
    url(r'^UpdateCustomers/(?P<pk>\d+)/$', UpdateCustomer.as_view(), name='update_customer'),
    url(r'^DeleteCustomers/(?P<pk>\d+)/$', DeleteCustomer.as_view(), name='delete_customer'),
    url(r'Customers/(?P<pk>\d+)/$', CustomerDetail.as_view(), name='detailed_customer'),
]

