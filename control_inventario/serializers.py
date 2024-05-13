from rest_framework import serializers

from .models import Inventario

class CantidadStockSerializer(serializers.Serializer):
    producto = serializers.CharField()
    cantidad_stock = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'producto': instance[0],
            'cantidad_stock': instance[1]
        }
