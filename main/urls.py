# urls.py - Variant 1: certificate_number bo'yicha
from django.urls import path
from . import views

urlpatterns = [
    path('<str:certificate_number>/', views.certificate_detail, name='certificate_detail'),
]