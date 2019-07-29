from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def register(request):
    return render(request, 'register.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def tryit(request):
    return render(request, 'tryit.html', {})

def greyscale(request):
    return render(request, 'greyscale.html', {})

def login(request):
    return render(request, 'login_choice.html', {})