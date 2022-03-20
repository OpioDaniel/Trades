from django.db import models


class Subjects(models.Model):
    subject_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.subject_name


class Levels(models.Model):
    level_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.level_name


class StudentRegistration(models. Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    subjects = models.ForeignKey(Subjects, null=False, on_delete=models.CASCADE)
    levels = models.ForeignKey(Levels,  null=False, on_delete=models.CASCADE)
    former_school = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        upload_to='registration/',
        default='registration/placeholder.png',
        max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


