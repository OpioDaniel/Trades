from django.contrib import admin
from .models import StudentRegistration, Levels, Subjects

admin.site.register(StudentRegistration)
admin.site.register(Subjects)
admin.site.register(Levels)
# Register your models here.
