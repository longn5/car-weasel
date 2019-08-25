from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from dataAPI import api as API
from django.http import HttpResponse, JsonResponse
import json

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
    if request.method == "POST":
        print("POST with authenticated user")
        if request.user.is_authenticated:
            userid = request.user.id

            v = list(request.POST.items())
            print("Items in POST:")
            print(v)
            v.sort(key=lambda tup: tup[0])
            for x in v:
                print(x)
            
            addstr = request.read().decode('utf-8')
            print("Request read")
            print(addstr)
            #vehicles = json.loads(addstr)
            #vstr = json.dumps(vstr)
            #print(vstr)
        else:
            return JsonResponse({'response': "Must Be Authenticated to POST"})
    elif request.method == "GET":
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