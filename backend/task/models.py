from django.db import models
from ckeditor.fields import RichTextField 

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=100)
    task_description = RichTextField(blank=True)
    task_number = models.IntegerField()
    task_file_extension = models.CharField(max_length=100, blank=True)
    default_code = models.TextField(blank=True)
    instruction = RichTextField(blank=True)
    answer = models.TextField(blank=True)
    error_message = models.TextField(blank=True)

    def __str__(self):
        return self.task_name
