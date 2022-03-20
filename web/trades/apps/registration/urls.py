from django.urls import path
from.views import home

app_name = 'registration'

urlpatterns = [
    path('', home, name='home'),

]