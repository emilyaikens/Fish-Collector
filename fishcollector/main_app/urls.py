from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name='about_us')
]