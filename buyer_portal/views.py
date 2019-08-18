from django.shortcuts import render
from django.http import HttpResponse
from dataAPI import api as API

# Create your views here.

def buyer_login(request):
    return render(request, 'buyer_login.html', {})

def login(request):
    return render(request, 'templates/register/login.html', {})

def allMakes(request):
    data = API.getAllMakes
    retData = str(data)
    return HttpResponse(retData, content_type="text/plain")
