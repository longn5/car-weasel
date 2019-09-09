from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('portal', views.portal, name="portal"),
    path('signup_choice', views.signup_choice, name="signup_choice"),
    path('api/datasets/allMakes', views.allMakes, name="allMakes"),
    path('api/datasets/getModels/<str:make>', views.getModelsForMake, name="getModelsFormake"),
    path('api/datasets/getModelYears/<str:make>/<str:model>', views.getYearsForMake, name="getYearsForMake"),
]