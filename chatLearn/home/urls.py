from django.urls import path
from .views import StudentDetailView, StudentListCreateView, CourseDetailView, CourseListView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-detail-view'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name="course-detail"),
]
