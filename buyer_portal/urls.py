from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('addPost', views.buyerAddPost, name="buyerAddPost"),
    path('signup', views.signup, name="signup"),
]