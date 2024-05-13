from django.urls import path
from . import views

app_name = 'control_inventario'



urlpatterns = [
    # Otras URLs de tu aplicación...
    path('cantidad-stock/', views.CantidadStock.as_view(), name='cantidad_stock'),
]


