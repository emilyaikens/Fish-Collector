from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name="home"),
    #http://localhost:8000/about-us
    path('about-us/', views.about_us, name='about_us'),
    #http://localhost:8000/fish
    path('fish/', views.fish_index, name='index'),
]