# from requests import Response
import requests
from .models import Course
from task.models import Task
from .serializers import CourseSerializer, CourseSerializerUpdate
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerUpdate


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializerUpdate 