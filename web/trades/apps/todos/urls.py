from django.conf.urls import url
from.views import home, add_citizen, view_detail, edit_detail, update_detail, delete_detail

app_name = 'todos'

urlpatterns = [
    url(r'home', home, name='home'),
    url(r'add_citizen', add_citizen, name='add_citizen'),
    url(r'^view_detail/(?P<pk>\d+)/$', view_detail, name='view_detail'),
    url(r'^edit_detail/(?P<pk>\d+)/$', edit_detail, name='edit_detail'),
    url(r'^update_detail/(?P<pk>\d+)/$', update_detail, name='update_detail'),
    url(r'^delete_detail/(?P<pk>\d+)/$', delete_detail, name='delete_detail'),
]