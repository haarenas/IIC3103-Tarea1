from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'web_api/home.html')

def personajes(request):
    return render(request, 'web_api/personajes.html')

def episodios(request):
    return render(request, 'web_api/episodios.html')
