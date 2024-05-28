from django.contrib import admin

# Register your models here.

from .models import Compra, DetalleCompra

class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('producto', 'cantidad', 'importe')
        else:
            return ('importe',)
    
class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraInline]
    list_display = ('fecha', 'total', 'empleado')
    list_filter = ('fecha', 'empleado')
    search_fields = ('fecha', 'empleado')
    date_hierarchy = 'fecha'


admin.site.register(Compra, CompraAdmin)

