from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('sellerhome/', views.shome),
    path('seller_register/', views.s_register),
    path('seller_login/', views.seller_login_1),
    path('vehicle_details/', views.vehicledetails),
    path('seller_details_2/', views.seller_details_2),
    path('admin_valuation1/', views.valuation_4),
    path('after_accepet/', views.after_accept),
    path('accept/<int:id>/', views.send_approve),
    path('after_deny/', views.after_reject),
    path('deny/<int:id>/', views.send_deny),
    path('bid_2/', views.seller_bid)
]
