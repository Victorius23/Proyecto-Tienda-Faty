from django.contrib import admin
from .models import Categoria, Proveedor, Producto
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("nombre",)
        else:
            return ()

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                (
                    "Datos de la categoría",
                    {
                        "fields": (
                            "nombre",
                        ),
                    },
                )
            ]
        return fieldsets

admin.site.register(Categoria, CategoriaAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")
    search_fields = ("nombre", "telefono")
    list_filter = ("nombre", "telefono")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("nombre", "telefono")
        else:
            return ()

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                (
                    "Datos del proveedor",
                    {
                        "fields": (
                            "nombre",
                            "telefono",
                        ),
                    },
                )
            ]
        return fieldsets
    

admin.site.register(Proveedor, ProveedorAdmin)

#cuadro del historial de productos
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precioventa", "preciocompra", "categoria", "proveedor")
    search_fields = ("nombre", "categoria__nombre", "proveedor__nombre")
    list_filter = ("categoria", "proveedor")

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("nombre", "precioventa", "preciocompra", "categoria", "proveedor")
        else:
            return ()

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj:
            fieldsets = [
                (
                    "Datos del producto",
                    {
                        "fields": (
                            "nombre",
                            "precioventa",
                            "preciocompra",
                            "categoria",
                            "proveedor",
                        ),
                    },
                )
            ]
        return fieldsets

admin.site.register(Producto, ProductoAdmin)