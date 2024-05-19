
from django.urls import path

from .views import VentaPorEmpleado
from .views import UsuarioRegistrado


app_name = 'registration'

urlpatterns = [
    path('empleado-mas-ventas/', VentaPorEmpleado.as_view(), name='empleado_mas_ventas'),
    path('usuarios-registrados/', UsuarioRegistrado.as_view(), name='usuarios_registrados'),

]