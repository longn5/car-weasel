from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from dataAPI import api as API
from django.http import HttpResponse, JsonResponse
import json

def index(request):
    return render(request, 'greyscale.html', {})

def portal(request):
    if request.user.is_authenticated:   
        usrgrp = Group.objects.get(user=request.user).name
        
        if(usrgrp == 'seller'):
            return redirect('/seller_portal')
        elif(usrgrp == 'buyer'):
            return redirect('/buyer_portal')
        else:
            return redirect('logout')
    else:
        return redirect('login')

def signup_choice(request):
    return render(request, 'signup_choice.html', {})

def allMakes(request):
    data = API.getAllMakes()
    return JsonResponse({'makes': data})

def getModelsForMake(request, make):
    data = API.getAllModels(make)
    return JsonResponse({'models': data})

def getYearsForMake(request, make, model):
    data = API.getMakeYears(make, model)
    return JsonResponse({'years': data})