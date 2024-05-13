from django.urls import path

from .views import TotalVentasHoyApi

app_name = 'control_ventas'

urlpatterns = [
    path('total-ventas-hoy/', TotalVentasHoyApi.as_view(), name='total_ventas_hoy')
]
