from django.shortcuts import render, redirect
from django.urls import reverse
from.models import Citizen


def home(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        country = request.POST['country']
        Citizen.objects.create(full_name=full_name, country=country)
    citizens = Citizen.objects.all()
    return render(request, 'todos/home.html', {'citizens': citizens})


def add_citizen(request):
    return render(request, 'todos/add_citizen.html',)


def view_detail(request, pk):
    citizens = Citizen.objects.get(id=pk)
    return render(request, 'todos/view_detail.html', {'citizens': citizens})


def edit_detail(request, pk):
    citizens = Citizen.objects.get(id=pk)
    citizens_ = Citizen.objects.all()
    context = {
        'citizens': citizens,
        'citizens_': citizens
    }
    return render(request, 'todos/add_citizen.html', context)


def update_detail(request, pk):
    citizens = Citizen.objects.get(id=pk)
    citizens.full_name = request.POST['full_name']
    citizens.country = request.POST['country']
    citizens.save()
    return redirect(reverse('todos:home'))


def delete_detail(request, pk):
    citizens = Citizen.objects.get(id=pk)
    citizens.delete()
    return redirect(reverse('todos:home'))


# Create your views here.
