from django.conf.urls import url
from .views import index, trial

app_name = "apewives"

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^t$', trial, name='trial'),

]
