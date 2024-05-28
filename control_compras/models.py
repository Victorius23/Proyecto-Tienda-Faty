from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User

from control_productos.models import Producto

from control_productos.models import Proveedor

# * receiver
from django.dispatch import receiver
# * post_save
from django.db.models.signals import post_save

from control_inventario.models import Inventario

from decimal import Decimal


class Compra(TimeStampedModel):
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.fecha} - {self.total}'
    

    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


class DetalleCompra(TimeStampedModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles_compra')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Subtotal', null=True, blank=True)
    
    def __str__(self):
        return f'{self.compra} - {self.producto}'
    
    class Meta:
        verbose_name = 'Detalle de Compra'
        verbose_name_plural = 'Detalles de Compras'
        
@receiver(models.signals.post_save, sender=DetalleCompra)
def actualizar_inventario_compra(sender, instance, created, **kwargs):

    compra = instance.compra
    if compra.total is None:
        compra.total = Decimal('0.0')

    compra.total += instance.importe
    compra.save()

    inventario = Inventario.objects.get(producto=instance.producto)
    inventario.cantidad_stock += instance.cantidad
    inventario.save()

    print(f'Inventario actualizado para {instance.producto.nombre}')





    
        
