from django.shortcuts import render

from neva.settings import GMAPlINK


def home(request):
    return render(request, 'home.html',{'GMAPlINK' : GMAPlINK})
