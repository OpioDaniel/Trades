from django.conf.urls import url
from.views import home, view_detail, delete_info, add_student, edit_info, update_info

app_name = 'student'

urlpatterns = [
    url(r'home', home, name='home'),
    url(r'add_student', add_student, name='add_student'),
    url(r'^view_detail/(?P<pk>\d+)/$', view_detail, name='view_detail'),
    url(r'^delete_info/(?P<pk>\d+)/$', delete_info, name='delete_info'),
    url(r'^edit_info/(?P<pk>\d+)/$', edit_info, name='edit_info'),
    url(r'^update_info/(?P<pk>\d+)/$', update_info, name='update_info'),
]