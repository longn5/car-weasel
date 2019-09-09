from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('addPost', views.buyerAddPost, name="buyerAddPost"),
    path('current_posts', views.current_posts, name="currentPosts"),
    path('signup', views.signup, name="buyer_signup"),
]