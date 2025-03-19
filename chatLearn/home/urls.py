from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='name'),
    path('index/', views.index, name='index'),
]