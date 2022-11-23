from django.db import models
from task.models import Task
from ckeditor.fields import RichTextField 
# import uuid


class Course(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    course_description = RichTextField(blank=True)
    course_interpreter = models.CharField(max_length=30, blank=True)
    courses_task = models.ManyToManyField(Task, blank=True)
            
    def __str__(self):
        return self.course_name


