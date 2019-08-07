from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'greyscale.html', {})