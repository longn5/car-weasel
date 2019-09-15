from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
import json

from .forms import SignUpForm
from .models import Buyer, BuyerPost

def welcome(request):
    if request.user.is_authenticated:
        userid = request.user.id

        return render(request, 'buyer_portal.html', {})
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN</h1>')


def current_posts(request):
    if request.user.is_authenticated:
        userid = request.user.id
        buyerObj = Buyer.objects.get(user=userid)
        buyerPosts = BuyerPost.objects.filter(userid=buyerObj)

        return render(request, 'current_posts.html', {
            'buyer_posts': buyerPosts,
            'post_count': str(len(buyerPosts)),
        })
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN</h1>')


# Method for a user to be able to add a post describing a vehicle.
def buyerAddPost(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            # request.POST.items() <-- This is empty, why?
            
            # Convert request data into json, then load said json into object.
            addstr = request.read().decode('utf-8')
            vehicles = json.loads(addstr)

            # Get the Buyer model associated with current user.
            userid = request.user.id
            buyerObj = Buyer.objects.get(user_id=userid)

            # For each vehicle found in the user submission, creat a new
            # BuyerPost object, associated with the user in question.
            count = 0
            try:
                for vehicle in vehicles['vehicles']:
                    bm = BuyerPost(
                        userid=buyerObj,
                        make=vehicle['make'],
                        model=vehicle['model'],
                        year=vehicle['year']
                    )
                    bm.save()
                    count = count + 1

                return JsonResponse({
                    'status': 'success',
                    'added': str(count),
                    'total': str(vehicles['count'])
                    })
            
            except Buyer.DoesNotExist:
                return JsonResponse({
                    'status': 'failure',
                    'added': str(count),
                    'total':  str(vehicles['count'])
                    })

        else:
            return JsonResponse({'response': "Must Be Authenticated to POST"})
    elif request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'buyer_dash_addPost.html', {})

    return redirect('login')


# Method for either serving the signup form, or processing a sent one.
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