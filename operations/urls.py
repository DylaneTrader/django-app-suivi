from django.urls import path
from . import views

app_name = 'operations'

urlpatterns = [
    path('nouvelle/', views.nouvelle_operation, name='nouvelle_operation'),
    path('suivi/', views.suivi_collecte, name='suivi_collecte'),
]
