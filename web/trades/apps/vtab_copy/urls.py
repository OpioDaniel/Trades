from django.conf.urls import url
from.views import(home, add_tab, get_tabs_from_table, activate_function, delete_tab, \
                  tab_div_content, update_text_tab)

app_name = 'vtab'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^add_tab$', add_tab, name='add_tab'),
    url(r'^get_tabs_from_table$', get_tabs_from_table, name='get_tabs_from_table'),
    url(r'^delete_tab$', delete_tab, name='delete_tab'),
    url(r'^update_text_tab$', update_text_tab, name='update_text_tab'),
    url(r'^activate_function$', activate_function, name='activate_function'),
    url(r'^tab_div_content$', tab_div_content, name='tab_div_content'),

]