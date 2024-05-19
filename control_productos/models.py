from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precioventa = models.DecimalField(max_digits=10, decimal_places=2,
                                      #* nombre del campo
                                        verbose_name='Precio de Venta')
    preciocompra = models.DecimalField(max_digits=10, decimal_places=2,
                                        #* nombre del campo
                                        verbose_name='Precio de Compra')
    descripcion = models.TextField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen_producto = models.ImageField(upload_to='productos', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

