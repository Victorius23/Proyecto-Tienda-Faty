from django.shortcuts import render
from .models import Venta
from rest_framework import viewsets
from .serializers import VentaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.


class VentaViewApi(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

# * api para conseguir el total de ventas de hoy
# * djangorestframework


class TotalVentasHoyApi(APIView):
    def get(self, request):
        total = Venta.objects.total_ventas_hoy()
        return Response({'total': total})


class ProductosMasVendidosApi(APIView):
    def get(self, request):
        productos = Venta.objects.productos_mas_vendidos()
        # * data
        data = [{'name': producto['detalles__producto__nombre'],
                 'value': producto['total']} for producto in productos]
        return Response(data)
