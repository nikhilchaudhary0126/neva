from django.shortcuts import render

from neva.settings import GMAP_LINK


def home(request):
    return render(request, 'home.html', {'GMAP_LINK': GMAP_LINK})
