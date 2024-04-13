from django.db import models
from django.dispatch import receiver

# Create your models here.

from control_productos.models import Producto


class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='inventario')
    cantidad_stock = models.PositiveIntegerField()
    ultima_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.producto} - {self.cantidad_stock}'
    
    class Meta:
        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventario'
        
        

# * asegurarse de crear inventario para cada vez que se cree un producto

@receiver(models.signals.post_save, sender=Producto)
def crear_inventario(sender, instance, created, **kwargs):
    if created:
        Inventario.objects.create(producto=instance, cantidad_stock=0)
        print(f'Inventario creado para {instance.nombre}')
    else:
        print(f'Inventario ya existe para {instance.nombre}')

        
        