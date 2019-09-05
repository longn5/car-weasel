from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
import json

from .forms import SignUpForm
from .models import Buyer

def welcome(request):
    if request.user.is_authenticated:   
        return render(request, 'buyer_portal.html', {'usergroup': 'buyer'})
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN</h1>')


def buyerAddPost(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            #userid = request.user.id

            # request.POST.items()
            # The above object is empty, why?
            
            # Convert request data into json, then dump said
            # json into object.
            addstr = request.read().decode('utf-8')
            vehicles = json.loads(addstr)
            vjson = json.dumps(vehicles)
            return JsonResponse({'response': "Success"})

        else:
            return JsonResponse({'response': "Must Be Authenticated to POST"})
    elif request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'buyer_dash_addPost.html', {})

    return redirect('login')


# Method for either serving the signup form, or 
# processing a sent one.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Add user to buyer group
            bg = Group.objects.get(name='buyer')
            bg.user_set.add(user)

            # Create instance of buyer model
            b = Buyer(user=user)
            b.save()

            # Login user and send to portal
            login(request, user)
            return redirect('/buyer_portal')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})