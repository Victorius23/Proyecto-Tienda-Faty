from django.contrib import admin

# Register your models here.

from .models import Inventario

#importe de la clase Sum
from django.db.models import Sum



#clase

class InventarioAdmin(admin.ModelAdmin):
    search_fields = ("producto", "ultima_actualizacion")
    list_filter = ("producto", "ultima_actualizacion")
    list_display = ("producto", "cantidad_stock", "ultima_actualizacion")



admin.site.register(Inventario, InventarioAdmin)

    
