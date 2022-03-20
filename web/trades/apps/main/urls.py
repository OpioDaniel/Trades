from django.conf.urls import url
from django.contrib.auth.views import (LoginView, LogoutView,)
from .views import (home, register,
                    view_profile, edit_user_profile, change_password,
                    MyPasswordResetView, MyPasswordResetDoneView,
                    MyPasswordResetConfirmView, MyPasswordResetCompleteView)

app_name = "main"

urlpatterns = [
    url(r'^$', home, name='home'),



    url(r'login/$', LoginView.as_view(template_name='main/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    url(r'^register/$', register, name='register'),

    url(r'^profile/$', view_profile, name='view_profile'),
    url(r'^profile/(?P<pk>\d+)/$', view_profile, name='view_profile_with_pk'),
    url(r'^profile/edit/user/$', edit_user_profile, name='edit_user_profile'),

    url(r'^change-password/$', change_password, name='change_password'),
    url(r'^reset-password/$', MyPasswordResetView.as_view(), name='reset_password'),
    url(r'^reset-password/done/$', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
 ]
