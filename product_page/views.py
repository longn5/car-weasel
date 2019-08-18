from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from dataAPI import api as API
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'greyscale.html', {})

def welcome(request):
    if request.user.is_authenticated:   
        usrgrp = Group.objects.get(user=request.user).name
        
        if(usrgrp == 'seller'):
            return render(request, 'seller_dash.html', {'usergroup': 'seller'})
        elif(usrgrp == 'buyer'):
            return render(request, 'buyer_dash.html', {'usergroup': 'buyer'})
        else:
            return render(request, 'welcome.html', {'usergroup': 'none'})
    else:
        return render(request, 'welcome.html', {'usergroup': 'not logged in'})

def goodbye(request):
    return render(request, TemplateView.as_view(template_name="templates/registration/logout.html"))


def buyerAddPost(request):
    if request.user.is_authenticated:
        usrgrp = Group.objects.get(user=request.user).name
        if usrgrp == 'buyer':
            return render(request, 'buyer_dash_addPost.html', {})

    return render(request, 'welcome.html', {})

def allMakes(request):
    data = API.getAllMakes()
    return JsonResponse({'makes': data})

def getModelsForMake(request, make):
    data = API.getAllModels(make)
    return JsonResponse({'models': data})

def getYearsForMake(request, make, model):
    data = API.getMakeYears(make, model)
    return JsonResponse({'years': data})