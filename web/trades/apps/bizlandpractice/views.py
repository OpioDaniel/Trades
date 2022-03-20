from django.shortcuts import render
from .models import BizlandMainWeb, FeaturedServices, AboutFL


def home(request):
    biz = BizlandMainWeb.objects.get(id=1)
    fs = FeaturedServices.objects.all()
    abfl = AboutFL.objects.all()
    return render(request, 'bizlandpractice/home.html', {'biz': biz, 'fs': fs, 'abfl': abfl})


