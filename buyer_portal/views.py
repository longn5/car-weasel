from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from dataAPI import api as API
import json

def allMakes(request):
    data = API.getAllMakes
    retData = str(data)
    return HttpResponse(retData, content_type="text/plain")


def welcome(request):
    if request.user.is_authenticated:   
        return render(request, 'buyer_portal.html', {'usergroup': 'buyer'})
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN</h1>')


def buyerAddPost(request):
    if request.method == "POST":
        print("POST with authenticated user")
        if request.user.is_authenticated:
            #userid = request.user.id

            # request.POST.items()
            # The above object is empty, why?
            
            # Convert request data into json, then dump said
            # json into object.
            addstr = request.read().decode('utf-8')
            vehicles = json.loads(addstr)
            vjson = json.dumps(vehicles)
            print("From JSON")
            print(vjson)
            return JsonResponse({'response': "Success"})

        else:
            return JsonResponse({'response': "Must Be Authenticated to POST"})
    elif request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'buyer_dash_addPost.html', {})

    return redirect('login')