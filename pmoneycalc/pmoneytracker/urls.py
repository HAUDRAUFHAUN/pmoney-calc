from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('payments/new/', views.newpayment),
    path('dashboard/', views.dashboard),
    path('outlogged/', views.outlogged)
]
