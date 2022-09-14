from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fish
from .forms import SurveyForm

# Create your views here.

def home(request):
    return HttpResponse("<h1>Home Page</h1>")

def about_us(request):
    return render(request, 'about.html')

def fish_index(request):
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', {'fish':fish})

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fish/detail.html', {'fish':fish})

def add_survey(request, fish_id):
    return HttpResponse(f'add survey for {fish_id}')


class FishCreate(CreateView):
    model = Fish
    fields = '__all__'
    # fields = ['age', 'description'] - use this if you want to specify what the form asks for

    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))

class FishUpdate(UpdateView):
    model = Fish
    fields = '__all__'

    def get_success_url(self, **kwargs):
        return reverse('detail', args=(self.object.id, ))

class FishDelete(DeleteView):
    model = Fish
    success_url = '/fish/'