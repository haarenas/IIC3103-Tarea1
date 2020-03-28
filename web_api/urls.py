from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-R&M'),
    path('personajes/', views.personajes, name='personajes'),
    path('episodios/', views.episodios, name='episodios'),
]