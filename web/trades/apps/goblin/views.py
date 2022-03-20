from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Citizen
from django.contrib.auth.models import User, auth
from django.contrib import messages


def add_list(request):

    return render(request, 'goblin/add_list.html', {})


def home(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['country']
        city = request.POST['city']
        date_of_birth = request.POST['date_of_birth']
        origin = request.POST['origin']
        Citizen.objects.create(first_name=first_name, last_name=last_name, country=country, city=city,
                               date_of_birth=date_of_birth, origin=origin)
    citizens = Citizen.objects.all()
    return render(request, 'goblin/home.html', {'citizens': citizens})


def results(request, pk):
    citizens = Citizen.objects.get(id=pk)
    #print(1111111111111111111111111111111)
    #print(citizens)
    #print(1111111111111111111111111111111)
    return render(request, 'goblin/results.html', {'citizens': citizens})


def edit_list(request, pk):
    citizens_ = Citizen.objects.get(id=pk)
    citizens = Citizen.objects.all()
    context = {
        'citizens_': citizens_,
        'citizens': citizens
    }
    return render(request, 'goblin/add_list.html', context)


def update_list(request, pk):
    list_ = Citizen.objects.get(id=pk)
    #print(2222222222222222222222222222)
    #print(list_)
    #print(2222222222222222222222222222)
    #print(list_.first_name)
    #print(2222222222222222222222222222)
    list_.first_name = request.POST['first_name']
    #print(1111111111111111111111111111)
    #print(list_.first_name)
    #print(111111111111111111111111111)
    list_.last_name = request.POST['last_name']
    list_.country = request.POST['country']
    list_.city = request.POST['city']
    list_.origin = request.POST['origin']
    list_.date_of_birth = request.POST['date_of_birth']
    list_.save()
    return redirect(reverse('goblin:home'))


def delete_list(request, pk):
    citizens = Citizen.objects.get(id=pk)
    citizens.delete()
    return redirect(reverse('goblin:home'))
