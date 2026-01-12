from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Operation
from clients.models import Client

@login_required
def nouvelle_operation(request):
    """Create a new operation"""
    if request.method == 'POST':
        client_id = request.POST.get('client')
        type_operation = request.POST.get('type_operation')
        montant = request.POST.get('montant')
        status = request.POST.get('status')
        description = request.POST.get('description')
        date_operation = request.POST.get('date_operation')
        
        try:
            client = Client.objects.get(id=client_id)
            Operation.objects.create(
                client=client,
                type_operation=type_operation,
                montant=montant,
                status=status,
                description=description,
                date_operation=date_operation,
                created_by=request.user
            )
            messages.success(request, 'Opération créée avec succès!')
            return redirect('operations:nouvelle_operation')
        except Exception as e:
            messages.error(request, f'Erreur lors de la création: {str(e)}')
    
    clients = Client.objects.all().order_by('nom', 'prenom')
    return render(request, 'operations/nouvelle_operation.html', {'clients': clients})

@login_required
def suivi_collecte(request):
    """Track collections with tabs for weekly, monthly, annual, and historical"""
    today = timezone.now().date()
    
    # Get tab parameter
    tab = request.GET.get('tab', 'hebdo')
    
    # Filter operations based on user role
    if request.user.role == 'commercial':
        operations_qs = Operation.objects.filter(created_by=request.user)
    else:
        operations_qs = Operation.objects.all()
    
    # Calculate date range based on tab
    if tab == 'hebdo':
        start_date = today - timedelta(days=today.weekday())
        operations = operations_qs.filter(date_operation__gte=start_date)
        title = 'Suivi hebdomadaire'
    elif tab == 'mensuel':
        start_date = today.replace(day=1)
        operations = operations_qs.filter(date_operation__gte=start_date)
        title = 'Suivi mensuel'
    elif tab == 'annuel':
        start_date = today.replace(month=1, day=1)
        operations = operations_qs.filter(date_operation__gte=start_date)
        title = 'Suivi annuel'
    else:  # historique
        operations = operations_qs.all()
        title = 'Historique complet'
    
    operations = operations.select_related('client', 'created_by').order_by('-date_operation', '-created_at')
    
    # Calculate totals
    total_montant = operations.aggregate(total=Sum('montant'))['total'] or 0
    total_count = operations.count()
    
    context = {
        'operations': operations,
        'tab': tab,
        'title': title,
        'total_montant': total_montant,
        'total_count': total_count,
    }
    
    return render(request, 'operations/suivi_collecte.html', context)
