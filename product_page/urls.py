from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('', views.greyscale, name="greyscale"),
    # path('about', views.about, name="about"),
    # path('register', views.register, name="register"),
    # path('tryit', views.tryit, name="tryit"),
    # path('contact', views.contact, name="contact"),
    path('login', views.login, name="login"),
]