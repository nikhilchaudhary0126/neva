from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def applogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.success(request, "Incorrect details! Please try again.")
            return render(request, 'login.html', {'form': AuthenticationForm()})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
