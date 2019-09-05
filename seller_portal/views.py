from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .models import Seller

def index(request):
    if request.user.is_authenticated:
        return render(request, 'seller_dash.html', {})
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN, ASSHOLE</h1>')

# Method for either serving for processing a Seller signup form
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            # Add user to seller group
            sg = Group.objects.get(name='seller')
            sg.user_set.add(user)

            # Create instance of Seller model
            s = Seller(user=user)
            s.save()

            # Login user and send to portal
            login(request, user)
            return redirect('/seller_portal')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})