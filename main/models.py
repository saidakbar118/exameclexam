# models.py
from django.db import models

class Certificate(models.Model):
    certificate_number = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Sertifikat raqami",
        primary_key=True  # Agar raqam unikal bo'lsa, primary key qilishimiz mumkin
    )
    certificate_image = models.FileField(
        upload_to='certificates/',
        verbose_name="Sertifikat fayli"
    )

    
    def __str__(self):
        return f"Sertifikat {self.certificate_number}"
    
    class Meta:
        verbose_name = "Sertifikat"
        verbose_name_plural = "Sertifikatlar"