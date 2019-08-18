from django.urls import path

from . import views

urlpatterns = [
    path('portal/buyer/addPost', views.buyerAddPost, name="buyerAddPost"),
    path('portal/buyer/api/datasets/allMakes', views.allMakes, name="allMakes"),
    path('portal/buyer/api/getModels/<str:make>', views.getModelsForMake, name="getModelsForMake"),
    path('portal/buyer/api/getModelYears/<str:make>/<str:model>', views.getYearsForMake, name="getYearsForMake"),
    path('portal', views.welcome, name="welcome"),
    path('', views.index, name="index"),
]