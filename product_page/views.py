from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'greyscale.html', {})

def login_choice(request):
    return render(request, 'login_choice.html', {})

def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'madeit.html', {})
    else:
        return render(request, 'failed.html', {})