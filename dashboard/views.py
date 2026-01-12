from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import datetime, timedelta
from operations.models import Operation
from clients.models import Client

@login_required
def dashboard_home(request):
    """Main dashboard with statistics and charts"""
    today = timezone.now().date()
    
    # Calculate date ranges
    start_of_week = today - timedelta(days=today.weekday())
    start_of_month = today.replace(day=1)
    start_of_year = today.replace(month=1, day=1)
    
    # Filter operations based on user role
    if request.user.role == 'commercial':
        operations_qs = Operation.objects.filter(created_by=request.user)
    else:
        operations_qs = Operation.objects.all()
    
    # Calculate statistics
    total_operations = operations_qs.count()
    total_clients = Client.objects.count()
    
    # Weekly stats
    weekly_operations = operations_qs.filter(date_operation__gte=start_of_week)
    weekly_total = weekly_operations.aggregate(total=Sum('montant'))['total'] or 0
    
    # Monthly stats
    monthly_operations = operations_qs.filter(date_operation__gte=start_of_month)
    monthly_total = monthly_operations.aggregate(total=Sum('montant'))['total'] or 0
    
    # Recent operations
    recent_operations = operations_qs.select_related('client', 'created_by')[:10]
    
    # Operations by type
    operations_by_type = operations_qs.values('type_operation').annotate(
        count=Count('id'),
        total=Sum('montant')
    )
    
    # Monthly data for chart (last 6 months)
    monthly_data = []
    for i in range(6):
        month_date = today - timedelta(days=30*i)
        month_start = month_date.replace(day=1)
        if i > 0:
            month_end = (today - timedelta(days=30*(i-1))).replace(day=1)
        else:
            month_end = today
        
        month_ops = operations_qs.filter(
            date_operation__gte=month_start,
            date_operation__lt=month_end
        )
        monthly_data.insert(0, {
            'month': month_start.strftime('%B'),
            'total': float(month_ops.aggregate(total=Sum('montant'))['total'] or 0)
        })
    
    context = {
        'total_operations': total_operations,
        'total_clients': total_clients,
        'weekly_total': weekly_total,
        'monthly_total': monthly_total,
        'recent_operations': recent_operations,
        'operations_by_type': operations_by_type,
        'monthly_data': monthly_data,
    }
    
    return render(request, 'dashboard/home.html', context)
