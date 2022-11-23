import uuid
from django.db import models
from task.models import Task
from ckeditor.fields import RichTextField 

# Create your models here.
class Solution(models.Model):
    uuid = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    status = models.BooleanField(default=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)
    solution_code = RichTextField(blank=True)
    result = RichTextField(blank=True)

    def __str__(self):
        return self.uuid