import json
import requests
from django.shortcuts import render, redirect
from home.forms import LocationForm
from home.models import Location
from neva.settings import GMAP_LINK, API_KEY, MAP_URL
from django.contrib import messages

def home(request):
    f1 = Location.objects.all()
    print(f1)
    data = Location.objects.get(id=1)
    print(data.latitude,data.longitude)

    f2 = Location.objects.all().filter(addresstype="Shelter")
    print(f2)

    return render(request, 'home.html', {'GMAP_LINK': GMAP_LINK})


def getLongitudeLatitude(combinedAddress):
    parameters = {
        "key": API_KEY,
        "location": combinedAddress
    }
    response = requests.get(MAP_URL, params=parameters)
    data = json.loads(response.text)
    return data


def createPost(request):
    if request.method == "POST":
        addresstype = request.POST['addresstype']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        form = LocationForm(request.POST)
        if form.is_valid():
            if addresstype and address and city and state:
                combinedAddress = address + "," + city + "," + state
                data = getLongitudeLatitude(combinedAddress)
                longitude = data['results'][0]['locations'][0]['displayLatLng']['lng']
                latitude = data['results'][0]['locations'][0]['displayLatLng']['lat']

                f = Location(address=address, city=city, state=state, addresstype=addresstype, latitude=latitude,
                             longitude=longitude)

                f.save()
                return redirect('home')
            else:
                messages.error(request, "Post failed! Please enter all details.")
    return render(request, 'createPost.html', {"form": LocationForm})