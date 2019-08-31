from django.shortcuts import render, redirect
from django.http import HttpResponse
from dataAPI import api as API

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
            return render(request, 'buyer_dash_addPost.html', {})

    return redirect('login')