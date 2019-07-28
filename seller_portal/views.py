from django.shortcuts import render

# Create your views here.
def seller_login(request):
    return render(request, 'seller_login.html', {})