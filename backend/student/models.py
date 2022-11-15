from django.db import models
from courses.models import Course

# Create your models here.
class Student(models.Model):
    email = models.EmailField(blank=True)
    courses = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return self.email