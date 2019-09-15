from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
import json

from .forms import SignUpForm
from .models import Seller, SellerPost

# Method for serving the Seller Dashboard upon login.
# Also handles Seller uploading inventory via Dashboard landing page.
def index(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            res = consume_seller_post(request)
            return JsonResponse({'status': str(res)})
        else:
            return JsonResponse({'response': 'you must be logged in to POST'})
    else:
        if request.user.is_authenticated:
            return render(request, 'seller_dash.html', {})
        else:
            return HttpResponse('<h1>YOU MUST BE LOGGED IN</h1>')



# Method for handling view that displays inventory
def inventory(request):
    if request.user.is_authenticated:
        # Fetch data associated with Seller
        userid = request.user.id
        sellerObj = Seller.objects.get(user=userid)
        sellerPosts = SellerPost.objects.filter(userid=sellerObj)

        return render(request, 'seller_inventory.html', {
            'seller_inventory': sellerPosts,
            'post_count': str(len(sellerPosts)),
        })
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN, ASSHOLE</h1>')



# Method for consuming a Seller's vehicle upload. This method should only
# be called after a Seller has been authenticated. 
def consume_seller_post(request):
    # Convert request data into json, then load said json into object
    uploadStr = request.read().decode('utf-8')
    vehicles = json.loads(uploadStr)

    # Get the Seller model associated with current user.
    userid = request.user.id
    sellerObj = Seller.objects.get(user_id=userid)

    # For each vehicle uploaded, instantiate the associated Model and save it.
    count = 0
    try:
        for vehicle in vehicles['vehicles']:
            sellerModel = SellerPost(
                userid = sellerObj,
                cylinders = vehicle['cylinders'],
                doors = vehicle['doors'],
                drive = vehicle['drive'],
                make = vehicle['make'],
                model = vehicle['model'],
                series = vehicle['series'],
                trim = vehicle['trim'],
                vin = vehicle['vin'],
                year = vehicle['year']
            )
            sellerModel.save()
            count = count + 1

        return count
  
    except (Seller.DoesNotExist, SellerPost.DoesNotExist):
        return 0


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