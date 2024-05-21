from django.urls import path

from .views import TotalVentasHoyApi, ProductosMasVendidosApi,VentasRealizadasHoy,GananciasPorMes
from .views import obtener_peso_bascula


app_name = 'control_ventas'

urlpatterns = [
    path('total-ventas-hoy/', TotalVentasHoyApi.as_view(), name='total_ventas_hoy'),
    path(
        'productos-mas-vendidos/', ProductosMasVendidosApi.as_view(), name='productos_mas_vendidos'),
    path('ventas-realizadas-hoy/', VentasRealizadasHoy.as_view(), name='ventas_realizadas_hoy'),
    path('ganancias-mes/', GananciasPorMes.as_view(), name='ganancias_mes'),
    path('obtener-peso-bascula/', obtener_peso_bascula, name='obtener_peso_bascula'),


]
