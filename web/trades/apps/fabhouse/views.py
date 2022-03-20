from django.shortcuts import render, redirect
from.models import CatalogCategorySections
from.models import Page
from.models import CatalogCategorySectionsSub


def get_param(page=None):
    params = {'logo_1': "Fab_House_Logo_Web.png"}
    Page
    if page == 'junior':
        params['title_1'] = 'We deliver all around East Africa'
        params['image_1'] = "SIBU_LL_ELEGANZA_GOLD.jpg"
        params['image_2'] = "Fab_House_Van_1.png"
        params['changing_list'] = '{"strings":["Uganda","Kenya ","Tanzania ","Rwanda","South Sudan","Malawi","Botswana ","South Africa"],"type_speed":50,"back_speed":100,"start_delay":1000,"back_delay":1000,"loop":true,"show_cursor":false,"cursor":"|"}'
    elif page == 'catalog':
        categories =CatalogCategorySectionsSub.all()
        params['section1'] = categories
        print(params)
    return params


def home(request):
    params=get_param()
    params['title_1'] = 'We deliver all around East Africa'
    params['image_2'] = "SIBU_LL_ELEGANZA_GOLD.jpg"
    params['image_1'] = "Fab_House_Van_1.png"
    params[
        'changing_list'] = '{"strings":["Uganda","Kenya ","Tanzania ","Rwanda","South Sudan","Malawi","Botswana ","South Africa"],"type_speed":50,"back_speed":100,"start_delay":1000,"back_delay":1000,"loop":true,"show_cursor":false,"cursor":"|"}'

    return render(request, 'fabhouse/home.html',params)


def catalog(request):
    logo_1 = "Fab_House_Logo_Web.png"
    sections=CatalogCategorySections.objects.filter(page__page_name='catalog').all()

    return render(request, 'fabhouse/catalog.html',{'sections': sections,'logo_1':logo_1})


def about(request):
    params = get_param()
    return render(request, 'fabhouse/about.html',params)


def contact(request):
    params = get_param()
    return render(request, 'fabhouse/contact.html',params)


def gallery(request):
    params = get_param()
    return render(request, 'fabhouse/gallery.html',params)





