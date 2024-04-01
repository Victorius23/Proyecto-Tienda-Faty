from django.db import models

# Create your models here.

from control_productos.models import Producto


class Inventario(models.Model):
    Producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_stock = models.PositiveIntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Producto} - {self.cantidad_stock}'
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
        