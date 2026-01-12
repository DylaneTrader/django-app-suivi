from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """Custom user model with role field"""
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('commercial', 'Commercial'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='commercial')
    phone = models.CharField(max_length=20, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Notification(models.Model):
    """Notification model for user alerts"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
