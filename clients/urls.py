from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('', views.suivi_client, name='suivi_client'),
    path('<int:client_id>/', views.client_detail, name='client_detail'),
]
