from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    #path('/login', include('django.contrib.auth.urls')),
]