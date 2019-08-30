from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portal', views.welcome, name="welcome"),
    path('api/datasets/allMakes', views.allMakes, name="allMakes"),
    path('api/datasets/getModels/<str:make>', views.getModelsForMake, name="getModelsFormake"),
    path('api/datasets/getModelYears/<str:make>/<str:model>', views.getYearsForMake, name="getYearsForMake"),
]