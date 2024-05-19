from django.urls import path

from .views import TotalVentasHoyApi, ProductosMasVendidosApi,VentasRealizadasHoy,GananciasPorMes

app_name = 'control_ventas'

urlpatterns = [
    path('total-ventas-hoy/', TotalVentasHoyApi.as_view(), name='total_ventas_hoy'),
    path(
        'productos-mas-vendidos/', ProductosMasVendidosApi.as_view(), name='productos_mas_vendidos'),
    path('ventas-realizadas-hoy/', VentasRealizadasHoy.as_view(), name='ventas_realizadas_hoy'),
    path('ganancias-mes/', GananciasPorMes.as_view(), name='ganancias_mes')

]
