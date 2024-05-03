from django import forms

from .models import Venta, DetalleVenta


# * detalle de venta
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ('producto', 'cantidad', 'importe')
        
    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        cantidad = cleaned_data.get('cantidad')
        
        if cantidad > producto.inventario.cantidad_stock:
            raise forms.ValidationError('No hay stock suficiente para el producto')
        
        return cleaned_data
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.importe = instance.producto.precioventa * instance.cantidad
        
        if commit:
            instance.save()
            
        return instance