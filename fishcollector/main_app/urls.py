from django.urls import path
from . import views

urlpatterns = [
    
    # http://localhost:8000
    path('', views.home, name="home"),

    #http://localhost:8000/about-us
    path('about-us/', views.about_us, name='about_us'),

    #http://localhost:8000/fish
    path('fish/', views.fish_index, name='index'),

    #http://localhost:8000/fish/1
    path('fish/<int:fish_id>/', views.fish_detail, name='detail'), 

    # http://localhost:8000/fish/create/
    path('fish/create/', views.FishCreate.as_view(), name='fish_create'), 

    # http://localhost:8000/fish/1/update
    path('fish/<int:pk>/update/', views.FishUpdate.as_view(), name='fish_update'),

    # http://localhost:8000/fish/1/delete
    path('fish/<int:pk>/>delete/', views.FishDelete.as_view(), name='fish_delete'),

    # http://localhost:8000/fish/1/add_survey/
    path('fish/<int:fish_id>/add_survey/', views.add_survey, name="add_survey"),

    # http://localhost:8000/fish/1/assoc_collector/1/
    path('fish/<int:fish_id>/assoc_collector/<int:collector_id>/', views.assoc_collector, name='assoc_collector'),

    # http://localhost:8000/collectors/
    path('collectors/', views.CollectorList.as_view(), name='collectors_index'),

    # http://localhost:8000/collectors/1/
    path('collectors/<int:pk>/', views.CollectorDetail.as_view(), name='collectors_detail'),

    # http://localhost:8000/collectors/create/
    path('collectors/create/', views.CollectorCreate.as_view(), name='collectors_create'),

    # http://localhost:8000/collectors/1/update/
    path('collectors/<int:pk>/update/', views.CollectorUpdate.as_view(), name='collectors_update'),
    
    # http://localhost:8000/collectors/1/delete/
    path('collectors/<int:pk>/delete/', views.CollectorDelete.as_view(), name='collectors_delete'),
]