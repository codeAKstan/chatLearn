from django.shortcuts import render, HttpResponse

# Create your views here

def home(request):
    return HttpResponse("Hello world")

def index(request):
    return render(request, 'home/index.html' )