from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Fish, Collector
from .forms import SurveyForm
# from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'about.html')

def fish_index(request):
    fish = Fish.objects.all()
    return render(request, 'fish/index.html', {'fish':fish})

def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    collectors_fish_doesnt_have = Collector.objects.exclude(id__in = fish.collectors.all().values_list('id'))
    survey_form = SurveyForm()
    return render(
        request, 
        'fish/detail.html', 
        {'fish':fish , 'survey_form':survey_form, 'collectors': collectors_fish_doesnt_have}
    )

def add_survey(request, fish_id):
    #print(request.POST['date']) <-- this allows us to see what's been entered into the form. the request.
    form = SurveyForm(request.POST)
    if form.is_valid():
        new_survey = form.save(commit=False) #commit=False because we need to assign a cat id
        new_survey.fish_id = fish_id # cat_id coming from url
        new_survey.save()    
    return redirect('detail', fish_id=fish_id)


class FishCreate(CreateView):
    model = Fish
    fields = ['commonName', 'sciName', 'habitat', 'quantity']
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

class CollectorList(ListView):
    model = Collector

class CollectorDetail(DetailView):
    model = Collector

class CollectorCreate(CreateView):
    model = Collector
    fields = '__all__'

class CollectorUpdate(UpdateView):
    model = Collector
    fields = ['name', 'vessel']

class CollectorDelete(DeleteView):
    model = Collector
    success_url = '/collectors/'

def assoc_collector(Request, fish_id, collector_id):
    Fish.objects.get(id=fish_id).collectors.add(collector_id)
    return redirect('detail', fish_id=fish_id)
        # redirect to detail refers to the url path named 'detail'
        # rdirect needs two params: the url and the ID, if there is one to pass