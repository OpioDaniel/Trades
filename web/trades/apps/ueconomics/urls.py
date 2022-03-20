from django.urls import path
from .views import (index, load_data, get_source_data, trial)

app_name = "ueconomics"

urlpatterns = [
    path(r'', index, name='index'),
    path(r'load_data', load_data, name='load_data'),
    path(r'get_source_data', get_source_data, name='get_source_data'),
    path(r'trial', trial, name='trial'),
]

