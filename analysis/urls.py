from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('analysishome/', views.ahome),
    path('analysis_register/', views.analysis_register),
    path('analysis_login/', views.analysis_login_1),
    path('vehicledetails2/', views.vehicle_details_2),
    path('analysis__team/', views.analysis_team_1),
    path('mechanical/', views.mechanical_verify),
    path('valuation1/', views.valuation_1),
    path('qotation1/<int:id>/', views.quotation),



]