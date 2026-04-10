# views.py - Variant 1: certificate_number bo'yicha
from django.shortcuts import render, get_object_or_404
from .models import Certificate

def certificate_detail(request, certificate_number):
    """Sertifikatni raqami bo'yicha ko'rsatish"""
    certificate = get_object_or_404(Certificate, certificate_number=certificate_number)
    return render(request, 'text.html', {'certificate': certificate})

