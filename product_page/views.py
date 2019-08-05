from django.shortcuts import render

def index(request):
    return render(request, 'greyscale.html', {})

def login(request):
    return render(request, 'login_choice.html', {})