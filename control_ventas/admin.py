from django.contrib import admin

# Register your models here.

from .models import Venta, DetalleVenta
#importa el precio del modelo Producto
from control_productos.models import Producto

class DetalleVentaInline(admin.TabularInline):

    def mostrar_precio(self, obj):
        return ''

    #modelo detalle de venta y precio del producto
    model = DetalleVenta
    #se muestra el producto, el precio, la cantidad y el importe
    fields = ('producto', 'cantidad', 'importe')

    #solo lectura
    readonly_fields = ('importe',)

    # * only read the fields

    extra = 1
class VentaAdmin(admin.ModelAdmin):
    
    readonly_fields = ('cliente',)
    inlines = [DetalleVentaInline]
    list_display = ('fecha', 'cliente', 'total')
    readonly_fields = ('total', 'estado', 'fecha')
   

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                ('Datos de la venta', {
                    'fields': ('cliente', 'total', 'estado', 'es_pedido', 'fecha'),
                }),
            ]

        else:
            fieldsets = [
                ('Datos de la venta', {
                    'fields': ('fecha',),
                }),
            ]


        return fieldsets

admin.site.register(Venta, VentaAdmin)