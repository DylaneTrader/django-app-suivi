from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from .models import Client

@login_required
def suivi_client(request):
    """Client tracking page with search and filtering"""
    search = request.GET.get('search', '')
    type_filter = request.GET.get('type', '')
    
    clients = Client.objects.all()
    
    if search:
        clients = clients.filter(
            nom__icontains=search
        ) | clients.filter(
            prenom__icontains=search
        ) | clients.filter(
            email__icontains=search
        )
    
    if type_filter:
        clients = clients.filter(type_client=type_filter)
    
    # Annotate with operation stats
    clients = clients.annotate(
        total_operations=Count('operations'),
        total_montant=Sum('operations__montant')
    ).select_related('commercial').order_by('nom', 'prenom')
    
    context = {
        'clients': clients,
        'search': search,
        'type_filter': type_filter,
    }
    
    return render(request, 'clients/suivi_client.html', context)

@login_required
def client_detail(request, client_id):
    """Client detail page with operation history"""
    client = get_object_or_404(Client, id=client_id)
    operations = client.operations.all().order_by('-date_operation')
    
    total_operations = operations.count()
    total_montant = operations.aggregate(total=Sum('montant'))['total'] or 0
    
    context = {
        'client': client,
        'operations': operations,
        'total_operations': total_operations,
        'total_montant': total_montant,
    }
    
    return render(request, 'clients/client_detail.html', context)
