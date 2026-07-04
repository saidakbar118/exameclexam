# admin.py
from django.contrib import admin
from .models import Certificate, certificate12

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['certificate_number']
    search_fields = ['certificate_number']
    
    
admin.site.register(certificate12)
