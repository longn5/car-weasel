from django.urls import path

from . import views

urlpatterns = [
    #path('', views.buyer_login, name="buyer_login"),
    path('', include('django.contrib.auth.urls')),
]