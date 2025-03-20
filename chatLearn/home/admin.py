from django.contrib import admin
from .models import Students, Course
# Register your models here.

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name'

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'name', 'code'