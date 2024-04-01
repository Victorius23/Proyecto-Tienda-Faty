from django.db import models
# * LAST modified and created at fields
from model_utils.models import TimeStampedModel

# * modelo usuario
from django.contrib.auth.models import User

from control_productos.models import Producto

# Create your models here.

class Venta(TimeStampedModel):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    #estado del pedido "en proceso", "entregado", "cancelado"


    estado = models.CharField(max_length=20, default='en proceso', choices=(
        ('en proceso', 'En Proceso'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ))
    
    es_pedido = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.cliente} - {self.fecha}'
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def decrementar_stock(self):
        for detalle in self.detalleventa_set.all():
            producto = detalle.producto
            producto.stock -= detalle.cantidad
            producto.save()

    def save(self, *args, **kwargs):
        # * si la venta no es un pedido
        if not self.es_pedido:
            self.decrementar_stock()
        super().save(*args, **kwargs)

class DetalleVenta(TimeStampedModel):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Subtotal')
    
    def __str__(self):
        return f'{self.venta} - {self.producto}'
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
