from django.shortcuts import render
from .models import StudentRegistration, Subjects, Levels


def home(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        former_school = request.POST['former_school']
        StudentRegistration.objects.create(first_name=first_name, last_name=last_name, former_school=former_school,
                                           )
    students = StudentRegistration.objects.all()
    subjects = Subjects.objects.all()
    levels = Levels.objects.all()
    return render(request, 'registration/home.html', {'students':students, 'subjects':subjects, 'levels':levels})
# Create your views here.
