from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portal', views.welcome, name="welcome"),
    path('goodbye', views.goodbye, name="goodbye"),
]