from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'greyscale.html', {})

def welcome(request):
    return render(request, 'welcome.html', {})