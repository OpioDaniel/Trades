from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Customer

# CRUD

def index(request):
    return render(request, 'dbillings/index.html', {'x': 500})


def customers(request):
    customers_ = Customer.objects.all()
    return render(request, 'dbillings/Customers_list.html', {'customers': customers_})


# customers views
# class CustomersView(ListView):
#     template_name = 'dbillings/customers_list.html'
#     model = Customer
#     context_object_name = 'customers'
#

class CustomerDetail(DetailView):
    template_name = 'dbillings/customers_detail.html'
    model = Customer
    context_object_name = 'customer'


# class CreateCustomer(CreateView):
#     model = Customer
#     fields = ['first_name', 'last_name']
#     #customer_form.html


def create_customer(request):
    print('------------')
    print('------------')
    print(request.method)
    print('------------')
    print('------------')

    if request.method == 'POST':
        customer = Customer.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
        return redirect(customer.get_absolute_url())
    return render(request, 'dbillings/data_entry_customers.html', {})


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



