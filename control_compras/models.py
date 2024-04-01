from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User

from control_productos.models import Producto

from control_productos.models import Proveedor


class Compra(TimeStampedModel):
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} - {self.proveedor} - {self.total}'
    
    def incrementar_stock(self):
        for detalle in self.detallecompra_set.all():
            producto = detalle.producto
            producto.stock += detalle.cantidad
            producto.save()

    def save(self, *args, **kwargs):
        self.incrementar_stock()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(TimeStampedModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal')
    
    def __str__(self):
        return f'{self.compra} - {self.producto}'
    
    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compras'




    
        
