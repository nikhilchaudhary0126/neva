import json
import requests
from django.shortcuts import render, redirect
from home.forms import LocationForm
from home.models import Location
from neva.settings import GMAP_LINK, API_KEY, MAP_URL, GOOGLE_MAPS_API_KEY
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

def applogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.success(request, "Incorrect details! Please try again.")
            return render(request, 'login.html', {'form': AuthenticationForm()})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if username and name and email and password1 and password2:
            if password1 == password2:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.first_name = name
                user.save()
                messages.success(request, "User created. Please login.")
                return redirect('/login')
            else:
                messages.error(request, "Passwords don't match")
                return render(request, 'registration.html', {"form": UserCreationForm()})
        else:
            messages.error(request, "Registration failed! Please try again.")
    return render(request, 'registration.html', {"form": UserCreationForm()})

def home(request):
    f1 = Location.objects.all()
    print(f1)
    # data = Location.objects.get(id=1)
    # print(data.latitude,data.longitude)

    # f2 = Location.objects.all().filter(addresstype="Shelter")
    # print(f2)

    return render(request, 'home.html', {'GMAP_LINK': GMAP_LINK})

def maps(request):
    f1 = Location.objects.all()
    # print(f1)
    # data = Location.objects.get(id=1)
    locationData = list()
    # print(data.latitude, data.longitude)
    for x in f1:
        locationData.append({
            'lat': x.latitude,
            'long': x.longitude,
            'type': x.addresstype})
    locationData = json.dumps(locationData)
    print(locationData)
    return render(request, 'map.html', {'gmap_key': GOOGLE_MAPS_API_KEY})

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
