from django.urls import path
from.views import home, acquisition, practise

app_name = 'bless'

urlpatterns = [
    path('', home, name='home'),
    path('acquisition', acquisition, name='acquisition'),
    path('practise', practise, name='practise')
]