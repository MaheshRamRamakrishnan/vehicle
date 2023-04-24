from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [

    path('admin_home/', views.adminhome),
    path('admin_login/', views.admin_login),
    path('seller_approve/', views.seller_approve),
    path('approve_seller/<int:id>/', views.approve_project),
    path('reject_seller/<int:id>/', views.reject_project),
    path('analysis_2/', views.analysis_t2),
    path('Quotation2/', views.valuation_2),
    path('send_seller/<int:id>/', views.send_Analysis),
]