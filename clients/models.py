from django.db import models
from django.conf import settings

# Create your models here.

class Client(models.Model):
    """Client model with all required fields"""
    TYPE_CHOICES = [
        ('A', 'Type A'),
        ('B', 'Type B'),
        ('C', 'Type C'),
    ]
    
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    type_client = models.CharField(max_length=1, choices=TYPE_CHOICES, default='C')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    commercial = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients'
    )
    
    class Meta:
        ordering = ['nom', 'prenom']
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    
    def __str__(self):
        return f"{self.nom} {self.prenom} ({self.type_client})"
    
    @property
    def full_name(self):
        return f"{self.nom} {self.prenom}"
