from django.contrib import admin

# Register your models here.

from .models import Venta, DetalleVenta

# importa el precio del modelo Producto
from control_productos.models import Producto

# importa librerias para transacciones y mensajes de error
from django.db import transaction
from django.core.exceptions import ValidationError
from django.db import models
from django import forms


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
    
    def save_formset(self, request, form, formset, change):
        try:
            with transaction.atomic():
                total = 0
                instances = formset.save(commit=False)
                for instance in instances:
                    if instance.producto.inventario.cantidad_stock < instance.cantidad:
                        from django.contrib import messages
                        messages.error(request, f"No hay suficiente stock para el producto {instance.producto}")
                        raise ValidationError(f"No hay suficiente stock para el producto {instance.producto}")
                    else:
                        instance.importe = instance.cantidad * instance.producto.precio
                        instance.producto.inventario.cantidad_stock -= instance.cantidad
                        total += instance.importe
                        instance.save()  # Mueve el guardado aquí
                form.instance.total = total
                form.instance.save()
                formset.save_m2m()
        except ValidationError as e:
            # Rollback manual de la transacción en caso de excepción
            transaction.set_rollback(True)
        return super().save_formset(request, form, formset, change)
         
        

        

    # * procesos extra de la venta y los detalles
    # def save_model(self, request, obj, form, change):
    #     if obj:
    #         with transaction.atomic():
    #             obj.empleado = request.user
    #             #calcula los importes de los detalles de la venta
    #             total = 0
    #             for detalle in obj.detalles.all():
    #                 detalle.importe = detalle.cantidad * detalle.producto.precio
    #                 detalle.producto.inventario.cantidad_stock -= detalle.cantidad
    #                 total += detalle.importe

    #             for detalle in obj.detalles.all():
    #                 detalle.producto.inventario.save()
    #                 detalle.save()

    #             obj.total = total

    #             obj.save()


admin.site.register(Venta, VentaAdmin)
