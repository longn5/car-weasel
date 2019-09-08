from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="seller_index"),
    path('inventory', views.inventory, name="seller_inventory"),
    path('signup', views.signup, name="seller_signup"),
]