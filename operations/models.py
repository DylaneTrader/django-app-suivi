from django.db import models
from django.conf import settings
from clients.models import Client

# Create your models here.

class Operation(models.Model):
    """Operation/Collection tracking model"""
    TYPE_CHOICES = [
        ('collecte', 'Collecte'),
        ('depot', 'Dépôt'),
        ('retrait', 'Retrait'),
    ]
    
    STATUS_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('annulee', 'Annulée'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='operations')
    type_operation = models.CharField(max_length=20, choices=TYPE_CHOICES, default='collecte')
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en_attente')
    description = models.TextField(blank=True)
    date_operation = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='operations_created'
    )
    
    class Meta:
        ordering = ['-date_operation', '-created_at']
        verbose_name = 'Opération'
        verbose_name_plural = 'Opérations'
    
    def __str__(self):
        return f"{self.type_operation} - {self.client.full_name} - {self.montant}€"
