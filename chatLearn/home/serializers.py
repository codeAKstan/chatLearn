from rest_framework import serializers
from .models import Students, Course

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'email', 'gender']

class CourseSerializer(serializers.ModelSerializer):
    students = StudentsSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'