# urls.py - Variant 1: certificate_number bo'yicha
from django.urls import path
from . import views

urlpatterns = [
    #path('<str:certificate_number>/', views.certificate_detail, name='certificate_detail'),
    path('certificate/1/', views.text_view),
    path('certificate/2/', views.text2_view),
]