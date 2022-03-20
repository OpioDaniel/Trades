from django.conf.urls import url
from .views import home, results, edit_list, add_list, delete_list, update_list

app_name = "goblin"

urlpatterns = [
    url(r'home', home, name='home'),
    url(r'add_list', add_list, name='add_list'),
    url(r'^results/(?P<pk>\d+)/$', results, name='results'),
    url(r'^editlist/(?P<pk>\d+)/$', edit_list, name='edit_list'),
    url(r'^Updatelist/(?P<pk>\d+)/$', update_list, name='update_list'),
    url(r'^deletelist/(?P<pk>\d+)/$', delete_list, name='delete_list'),

]

