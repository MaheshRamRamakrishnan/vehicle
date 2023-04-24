from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('managehome/', views.mhome),
    path('manage_register/', views.management_register),
    path('manage_login/', views.management_login_1),
    path('seller_details_3/', views.sellerdetails_2),
    path('send_admin/<int:id>/', views.send_Admin),
    path('comment1/<int:id>/', views.comment_1),
    path('seller_vehicle_2/', views.vehicle_details_1),
    path('send_analysis/<int:id>/', views.send_Analysis),
    path('accepted_seller/', views.after_seller_accept),
    path('rejected_seller/', views.after_seller_reject),
    path('smart_contract/<int:id>/', views.smart_contract),
    path('get_view/',views.get_view),
    path('encrypt/<int:id>/', views.get_input2),

]