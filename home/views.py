from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
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
