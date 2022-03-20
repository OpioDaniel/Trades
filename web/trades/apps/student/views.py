from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from.models import Students


def home(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        country = request.POST['country']
        Students.objects.create(full_name=full_name, country=country)
    students = Students.objects.all()
    return render(request, 'student/list.html', {'students': students})


def view_detail(request, pk):
    students_ = Students.objects.get(id=pk)
    return render(request, 'student/view_detail.html', {'students': students_})


def add_student(request):
    return render(request, 'student/add_student.html')


def delete_info(request, pk):
    students = Students.objects.get(id=pk)
    students.delete()
    return redirect(reverse('student:home'))


def edit_info(request, pk):
    students_ = Students.objects.get(id=pk)
    students = Students.objects.all()
    context = {
       'students_': students_,
       'students': students
    }
    return render(request, 'student/add_student.html', context)


def update_info(request, pk):
    students_ = Students.objects.get(id=pk)
    #print('----------before--------')
    #print(students_.country)
    #print(students_.country)
    students_.full_name = request.POST['full_name']
    students_.country = request.POST['country']
    #print('----------after--------')
    #print(students_.country)
    students_.save()
    return redirect(reverse('student:home'))

# Create your views here.
