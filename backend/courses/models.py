from django.db import models
from task.models import Task
# import uuid


class Course(models.Model):
    course_name = models.CharField(max_length=100, blank=True)
    course_description = models.TextField(blank=True)
    course_interpreter = models.CharField(max_length=30, blank=True)
    courses_task = models.ManyToManyField(Task, blank=True)
            
    def __str__(self):
        return self.course_name


# class TaskStatus(models.Model):
#     uuid = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
#     status = models.BooleanField(default=False)
#     task = models.ForeignKey(Task, on_delete=models.CASCADE)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.uuid

