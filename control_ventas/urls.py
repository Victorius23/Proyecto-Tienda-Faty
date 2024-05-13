from django.urls import path

from .views import TotalVentasHoyApi, ProductosMasVendidosApi

app_name = 'control_ventas'

urlpatterns = [
    path('total-ventas-hoy/', TotalVentasHoyApi.as_view(), name='total_ventas_hoy'),
    path(
        'productos-mas-vendidos/', ProductosMasVendidosApi.as_view(), name='productos_mas_vendidos')
]
