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