from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils import timezone
import csv
import json

@login_required
def export_center(request):
    """Export center for data export"""
    return render(request, 'exports/export_center.html')

@login_required
def export_operations_csv(request):
    """Export operations to CSV"""
    from operations.models import Operation
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="operations_{timezone.now().strftime("%Y%m%d")}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Date', 'Client', 'Type', 'Montant', 'Statut', 'Description'])
    
    operations = Operation.objects.select_related('client').order_by('-date_operation')
    for op in operations:
        writer.writerow([
            op.date_operation.strftime('%d/%m/%Y'),
            op.client.full_name,
            op.get_type_operation_display(),
            op.montant,
            op.get_status_display(),
            op.description
        ])
    
    return response

@login_required
def export_clients_csv(request):
    """Export clients to CSV"""
    from clients.models import Client
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="clients_{timezone.now().strftime("%Y%m%d")}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Nom', 'Prénom', 'Email', 'Téléphone', 'Type', 'Commercial'])
    
    clients = Client.objects.select_related('commercial').all()
    for client in clients:
        writer.writerow([
            client.nom,
            client.prenom,
            client.email,
            client.telephone,
            client.get_type_client_display(),
            client.commercial.get_full_name() if client.commercial else ''
        ])
    
    return response
