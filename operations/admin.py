from django.contrib import admin
from .models import Operation

# Register your models here.

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['date_operation', 'type_operation', 'client', 'montant', 'status', 'created_by', 'created_at']
    list_filter = ['type_operation', 'status', 'date_operation', 'created_at']
    search_fields = ['client__nom', 'client__prenom', 'description']
    date_hierarchy = 'date_operation'
    list_per_page = 20
