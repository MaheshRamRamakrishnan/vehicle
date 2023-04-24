from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('buyer_home/', views.bhome),
    path('buyer_register/', views.buyer_register),
    path('buyer_login/', views.buyer_login_1),
    path('buyer_details/', views.buyer_details),
    path('smart_contractcars/', views.after_smart_contract),
    path('buyer_bid/<int:id>/', views.Bid_buyer),
]