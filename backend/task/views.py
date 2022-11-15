from django.shortcuts import render

# Create your views here.
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
