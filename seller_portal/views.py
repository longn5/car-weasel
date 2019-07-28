from django.shortcuts import render

# Create your views here.
def seller_portal(request):
    return render(request, 'seller_portal.html', {})