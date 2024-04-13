from django.db import models
# * LAST modified and created at fields
from model_utils.models import TimeStampedModel

# * modelo usuario
from django.contrib.auth.models import User

from control_productos.models import Producto

from django.db import transaction
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.contrib import messages


# Create your models here.

class Venta(TimeStampedModel):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras', null=True, blank=True)
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas', null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    #estado del pedido "en proceso", "entregado", "cancelado"


    estado = models.CharField(max_length=20, default='en proceso', choices=(
        ('en proceso', 'En Proceso'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado')
    ))
    
    es_pedido = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.fecha}'
    
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

    def decrementar_stock(self):
        print("detalles:", self.detalles.all())
        for detalle in self.detalleventa_set.all():
            producto = detalle.producto
            print(producto.inventario)
            producto.inventario.cantidad_stock -= detalle.cantidad
            if producto.inventario.cantidad_stock < 0:
                raise ValidationError(f'No hay stock suficiente para el producto {producto}')

        for detalle in self.detalleventa_set.all():
            detalle.producto.save()

    # def save(self, *args, **kwargs):
    #     with transaction.atomic():
    #         try:
    #             super().save(*args, **kwargs)
    #             self.decrementar_stock()
                
    #         except Exception as e:
    #             # * rollback
    #             transaction.set_rollback(True)
    #             raise ValidationError('Error al guardar la venta: ' + str(e))
            

class DetalleVenta(TimeStampedModel):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    importe = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Subtotal', null=True, blank=True)
    
    def __str__(self):
        return f'{self.producto} - {self.cantidad} - {self.importe}'
    
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Ventas'
        
            
        
         

# from django.db import IntegrityError
# from django.core.exceptions import ValidationError
# from django.contrib import admin

# @receiver(models.signals.post_save, sender=DetalleVenta)
# def decrementar_stock(sender, instance, **kwargs):
#     producto = instance.producto
#     try:
#         producto.inventario.cantidad_stock -= instance.cantidad
#         producto.inventario.save()
#         producto.save()
#         print('Stock actualizado')
#     except IntegrityError:
#         mensaje = 'No hay suficiente stock disponible para el producto'
#         admin.ModelAdmin.message_user(None, mensaje, level=messages.ERROR)
        
        