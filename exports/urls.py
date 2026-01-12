from django.urls import path
from . import views

app_name = 'exports'

urlpatterns = [
    path('', views.export_center, name='export_center'),
    path('operations/csv/', views.export_operations_csv, name='export_operations_csv'),
    path('clients/csv/', views.export_clients_csv, name='export_clients_csv'),
]
