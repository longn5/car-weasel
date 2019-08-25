from django.urls import path, include

from . import views

urlpatterns = [
    #path('', views.buyer_login, name="buyer_login"),
    path('', include('django.contrib.auth.urls')),
]