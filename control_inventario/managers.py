from django.db import models


# * conseguir el producto y su cantidad_stock

class InventariosManager(models.Manager):

    def total_inventarios(self):
        # conseguir la cantidad_stock total de todos los productos
        return self.aggregate(total=models.Sum('cantidad_stock'))['total'] or 0

    def producto_y_stock(self):
        # conseguir el producto y su cantidad_stock
        return self.values_list('producto', 'cantidad_stock')


        
        
        
