from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventario
from .serializers import CantidadStockSerializer
from django.http import JsonResponse
from .models import Producto  # Asumiendo que Producto es tu modelo de productos



class CantidadStock(APIView):
    def get(self, request):
        inventarios = Inventario.objects.all()
        data = [{'producto': inv.producto.nombre, 'cantidad_stock': inv.cantidad_stock} for inv in inventarios]
        return JsonResponse(data, safe=False)

class CantidadProductos(APIView):
    def get(self, request):
        # espera que se le pa el id de un producto
        id_producto = request.GET.get('id_producto')
        inventarios = Inventario.objects.filter(producto_id=id_producto)
        data = [{'producto': inv.producto.nombre, 'cantidad_stock': inv.cantidad_stock} for inv in inventarios]
        return JsonResponse(data, safe=False)

