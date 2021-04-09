from django.db import models
from django.urls import reverse


class Student(models.Model):
    student_number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)

    # def get_absolute_url(self):
    #     return reverse('library:detailed_student', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name
