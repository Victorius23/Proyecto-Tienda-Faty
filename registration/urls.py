
from django.urls import path

from .views import EmpleadoMasVentas

app_name = 'registration'

urlpatterns = [
    path('empleado-mas-ventas/', EmpleadoMasVentas.as_view(), name='empleado_mas_ventas'),
]