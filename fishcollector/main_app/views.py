from django.shortcuts import render
from django.http import HttpResponse
from .models import Fish

# Create your views here.

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def about_us(request):
    return render(request, 'about.html')
