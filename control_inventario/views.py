from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventario
from .serializers import CantidadStockSerializer
from django.http import JsonResponse


class CantidadStock(APIView):
    def get(self, request):
        inventarios = Inventario.objects.all()
        data = [{'producto': inv.producto.nombre, 'cantidad_stock': inv.cantidad_stock} for inv in inventarios]
        return JsonResponse(data, safe=False)
