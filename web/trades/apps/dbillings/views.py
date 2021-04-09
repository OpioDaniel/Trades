from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Customer


def index(request):
    return render(request, 'dbillings/index.html', {})


def create_customer(request):
    if request.method == 'POST':
        customer = Customer.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        return redirect(customer.get_absolute_url())
    return render(request, 'dbillings/data_entry_customers.html', {})


class CustomerDetail(DetailView):
    template_name = 'dbillings/customers_detail.html'
    model = Customer
    context_object_name = 'customer'

#
# def create_customer(request):
#     print('------------')
#     print('------------')
#     print(request.method)
#     print('------------')
#     print('------------')
#
#     if request.method == 'POST':
#         customer = Customer.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
#         return redirect(customer.get_absolute_url())
#     return render(request, 'dbillings/data_entry_customers.html', {})
#




def customers(request):
    title_ = "Customers ............... "
    customers_ = Customer.objects.all()
    return render(request, 'dbillings/Customers_list.html', {
        'title': title_,
        'customers': customers_
    })
