from django.shortcuts import render
from .models import Towns


def index(request):
    towns=Towns.objects.all()
    return render(request, 'ugandatowns/index_.html',{'towns':towns})

def detailed_town(request,pk):
    towns = Towns.objects.get(pk=pk)
    return render(request,'ugandatowns/detailed_town.html',{'towns':towns})



