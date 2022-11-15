from rest_framework import serializers
from .models import Course
from task.models import Task
from task.serializers import TaskSerializer

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name', 'course_description', 'course_interpreter', 'courses_task']
        depth = 1

class CourseSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
