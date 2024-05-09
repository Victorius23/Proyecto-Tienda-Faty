from django.contrib import admin

# Register your models here.

from .models import Venta, DetalleVenta


from .forms import DetalleVentaForm


class DetalleVentaInline(admin.TabularInline):

    def mostrar_precio(self, obj):
        return ""

    # modelo detalle de venta y precio del producto
    model = DetalleVenta
    
    
    # se muestra el producto, el precio, la cantidad y el importe
    fields = ("producto", "cantidad", "importe")

    # solo lectura
    readonly_fields = ("importe",)

    # * only read the fields

    extra = 1

    form = DetalleVentaForm


class VentaAdmin(admin.ModelAdmin):

    inlines = [DetalleVentaInline]

    list_display = ("fecha", "cliente", "total")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("cliente", "total", "estado", "fecha", "es_pedido", "empleado")
        else:
            return ("total", "estado", "fecha")

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                (
                    "Datos de la venta",
                    {
                        "fields": (
                            "cliente",
                            "total",
                            "estado",
                            "es_pedido",
                            "fecha",
                            "empleado",
                        ),
                    },
                ),
            ]

        else:
            fieldsets = [
                (
                    "Datos de la venta",
                    {
                        "fields": ("fecha",),
                    },
                ),
            ]

        return fieldsets
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.empleado = request.user
        # obj.decrementar_stock()
        # # * obtener total de la venta
        # total = sum([detalle.importe for detalle in obj.detalles.all()])
        # obj.total = total
        # obj.save()
        
    
admin.site.register(Venta, VentaAdmin)


