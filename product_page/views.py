from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView

def index(request):
    return render(request, 'greyscale.html', {})

def welcome(request):
    if request.user.is_authenticated:
        usrgrp = Group.objects.get(user=request.user).name
        if(usrgrp == 'seller'):
            return render(request, 'seller_dash.html', {'usergroup': 'seller'})
        elif(usrgrp == 'buyer'):
            return render(request, 'welcome.html', {'usergroup': 'buyer'})
        else:
            return render(request, 'welcome.html', {'usergroup': usrgrp})
    else:
        return render(request, 'welcome.html', {'usergroup': 'not logged in'})

def goodbye(request):
    return render(request, TemplateView.as_view(template_name="templates/registration/logout.html"))