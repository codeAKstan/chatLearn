from django.db import models

# Create your models here.

class Students(models.Model):
    GENDER_CHOICES=[
        ('M', 'Male'), ('F', 'Female')
        ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=10)
    description = models.TextField()
    students = models.ManyToManyField(Students, related_name='courses')

    def __str__(self):
        return f"{self.name} {self.code}"