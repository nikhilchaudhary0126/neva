from django.shortcuts import render

from neva.settings import GMAP_LINK


def home(request):
    return render(request, 'home.html', {'GMAP_LINK': GMAP_LINK})

def maps(request):
    return render(request, 'map.html', {'GMAP_LINK': GMAP_LINK})
