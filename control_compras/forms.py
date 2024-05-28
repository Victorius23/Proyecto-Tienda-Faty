from .models import DetalleCompra
from control_inventario.models import Inventario
from django import forms

class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = ('producto', 'cantidad', 'importe')
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.importe = instance.producto.preciocompra * instance.cantidad
        
        if commit:
            instance.save()
        return instance