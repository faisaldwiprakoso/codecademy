from rest_framework import serializers
from .models import Task
# from courses.models import Course
# from courses.serializers import CourseSerializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"