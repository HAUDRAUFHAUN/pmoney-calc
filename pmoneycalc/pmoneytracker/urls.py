from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('payments/new/', views.newpayment),
    path('payments/delete/<int:p_id>/', views.deletepayment),
    path('dashboard/', views.dashboard),
]
