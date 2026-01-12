from django.contrib import admin
from .models import Client

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'email', 'telephone', 'type_client', 'commercial', 'created_at']
    list_filter = ['type_client', 'created_at']
    search_fields = ['nom', 'prenom', 'email', 'telephone']
    list_per_page = 20
