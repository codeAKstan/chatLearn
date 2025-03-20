from django.urls import path
from .views import student_list, course_list

urlpatterns = [
    path('students/', student_list, name='student-list'),
    path('courses/', course_list, name='course-list'),
]
