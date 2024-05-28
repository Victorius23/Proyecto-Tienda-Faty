from django.contrib import admin

# Register your models here.

from .models import Compra, DetalleCompra
from .forms import DetalleCompraForm


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('producto', 'cantidad', 'importe')
        else:
            return ('importe',)
    
    form = DetalleCompraForm


class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraInline]
    list_display = ("fecha", "total")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("total", "fecha",  "empleado")
        else:
            return ("total", "fecha")

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                (
                    "Datos de la compra",
                    {
                        "fields": (
                            "total",
                            "fecha",
                            "empleado",
                        ),
                    },
                ),
            ]

        else:
            fieldsets = [
                (
                    "Datos de la compra",
                    {
                        "fields": ("fecha",),
                    },
                ),
            ]

        return fieldsets

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.empleado = request.user


admin.site.register(Compra, CompraAdmin)
