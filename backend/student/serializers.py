from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        depth = 2


class StudentSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"