from django.shortcuts import render

# Create your views here.

def buyer_login(request):
    return render(request, 'buyer_login.html', {})