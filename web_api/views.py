from django.shortcuts import render
from django.http import HttpResponse
from .services import get_episodes, get_characters, get_locations, get_info

# Create your views here.
def home(request):
    lista_ep = [int(i+1) for i in range(31)]
    context = {
        'episodios': get_episodes(lista_ep)
    }
    return render(request, 'web_api/home.html', context)

def personajes(request):
    lista_pj = [int(i+1) for i in range(493)]
    context = {
        'title': 'Personajes',
        'personajes': get_characters(lista_pj)
    }
    return render(request, 'web_api/personajes.html', context)

def personaje(request, pj_id):
    context = {
        'title': 'Personaje',
        'personajes': get_characters([pj_id])[0]
    }
    return render(request, 'web_api/personaje.html', context)

def episodios(request):
    lista_ep = [int(i+1) for i in range(31)]
    context = {
        'title': 'Episodios',
        'episodios': get_episodes(lista_ep)
    }
    return render(request, 'web_api/episodios.html', context)

def episodio(request, ep_id):
    context = {
        'title': 'Episodio',
        'episodios': get_episodes([ep_id])[0]
    }
    return render(request, 'web_api/episodio.html', context)

def lugares(request):
    lista_loc = [int(i+1) for i in range(76)]
    context = {
        'title': 'Lugares',
        'lugares': get_locations(lista_loc)
    }
    return render(request, 'web_api/lugares.html', context)


def lugar(request, loc_id):
    context = {
        'title': 'Lugar',
        'lugares': get_locations([loc_id])[0]
    }
    return render(request, 'web_api/lugar.html', context)


def buscar(request):
    #if resquest.method != "GET":
    search_string = request.GET.get("busqueda")
    res_search = get_info(search_string)
    context = {
        'title': 'Busqueda',
        'personajes': {
            'encontro': True if res_search[0][0] else False,
            'resultado': res_search[0]
        },
        'lugares': {
            'encontro': True if res_search[1][0] else False,
            'resultado': res_search[1]
        },
        'episodios': {
            'encontro': True if res_search[2][0] else False,
            'resultado': res_search[2]
        }

    }
    
    return render(request, 'web_api/busqueda.html', context)
