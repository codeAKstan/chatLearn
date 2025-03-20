from django.shortcuts import render, HttpResponse
from .models import Students, Course
from .serializers import StudentsSerializer, CourseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def student_list(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)