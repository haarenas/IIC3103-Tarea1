from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-R&M'),
    path('personajes/', views.personajes, name='personajes'),
    path('personaje/<int:pj_id>', views.personaje, name='personaje'),
    path('episodios/', views.episodios, name='episodios'),
    path('episodio/<int:ep_id>', views.episodio, name='episodio'),
    path('lugares/', views.lugares, name='lugares'),
    path('lugar/<int:loc_id>', views.lugar, name='lugar'),
    path('buscar/', views.buscar, name='buscar'),
]