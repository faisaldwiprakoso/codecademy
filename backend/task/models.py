from django.db import models
# from courses.models import Course

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(blank=True)
    task_number = models.IntegerField()
    task_file_extension = models.CharField(max_length=10, blank=True)
    default_code = models.TextField(blank=True)

    def __str__(self):
        return self.task_name
