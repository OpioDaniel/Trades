from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Customer


def index(request):
    return render(request, 'dbillings/index.html', {'x': 500})


# def customers(request):
#     customers_ = Customer.objects.all()
#     return render(request, 'dbillings/customers.html', {'customers': customers_})


# customers views
class CustomersView(ListView):
    template_name = 'dbillings/customers_list.html'
    model = Customer
    context_object_name = 'customers'


class CustomerDetail(DetailView):
    template_name = 'dbillings/customers_detail.html'
    model = Customer
    context_object_name = 'customer'


class CreateCustomer(CreateView):
    model = Customer
    fields = ['first_name', 'last_name']
    #customer_form.html


class UpdateCustomer(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name']
    template_name = 'dbillings/customer_update_form.html'
    #template_name_suffix = '_update_form'
    #customer_update_form.html


class DeleteCustomer(DeleteView):
    model = Customer
    success_url = reverse_lazy('dbillings:list_Customer')
    #customer_confirm_delete.html



