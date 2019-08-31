from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.user.is_authenticated:
        return render(request, 'seller_dash.html', {})
    else:
        return HttpResponse('<h1>YOU MUST BE LOGGED IN, ASSHOLE</h1>')