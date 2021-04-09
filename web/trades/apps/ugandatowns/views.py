from django.shortcuts import render
from .models import Towns


def index(request):
    towns = Towns.objects.all()
    title = "Wonderful Uganda towns"
    return render(request, 'ugandatowns/index.html', {'towns': towns, 'title': title})


def detailed_town(request, pk):
    town = Towns.objects.get(id=pk)
    return render(request, 'ugandatowns/detailed_town.html', {'town': town})

